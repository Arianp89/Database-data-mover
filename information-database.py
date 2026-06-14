import mysql.connector
import os
import pickle
from config import *


# ✅ اصلاح 1: تعریف متغیرهای پیکربندی
# این متغیرها باید در فایل config.py تعریف شوند یا از اینجا دریافت شوند
# db_config = {'host': 'localhost', 'user': 'root', 'password': 'your_password'}
# database_name = 'your_database'


def get_relations(db_config, database_name):
    """
    دریافت تمام روابط بین جداول (Foreign Keys)
    """
    try:
        conn = mysql.connector.connect(**db_config, database=database_name)
        cur = conn.cursor(dictionary=True)
        cur.execute("""
        SELECT
            TABLE_NAME,
            COLUMN_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE TABLE_SCHEMA = DATABASE()
        """)
        relations = cur.fetchall()
        return relations
    except mysql.connector.Error as err:
        print(f"❌ خطا در دریافت روابط: {err}")
        return []
    finally:
        cur.close()
        conn.close()


# ✅ اصلاح 2: ساده‌سازی تابع get_list_of_table
def get_list_of_table(relations):
    """
    دریافت لیست تمام جداول براساس تعداد روابط
    اصلاح: حذف کد غیرضروری و ساده‌سازی منطق
    """
    table_count = {}
    
    # شمارش تعداد روابط برای هر جدول
    for rel in relations:
        table_name = rel['TABLE_NAME']
        
        if table_name not in table_count:
            table_count[table_name] = 0
        
        table_count[table_name] += 1
    
    # ترتیب جداول براساس تعداد روابط
    sorted_tables = sorted(table_count.items(), key=lambda x: x[1])
    table_list = [table_name for table_name, _ in sorted_tables]
    
    return table_list


# ✅ اصلاح 3: افزودن جلوگیری از SQL Injection
def get_table_data(table_name, db_config, database_name):
    """
    دریافت داده‌های یک جدول
    اصلاح: اضافه کردن بررسی نام جدول
    """
    # بررسی نام جدول برای جلوگیری از SQL Injection
    if not table_name.isalnum() and '_' not in table_name:
        print(f"❌ نام جدول نامعتبر: {table_name}")
        return []
    
    try:
        conn = mysql.connector.connect(**db_config, database=database_name)
        cur = conn.cursor(dictionary=True)
        
        # استفاده از backtick برای نام جدول
        SQL_Query = f"SELECT * FROM `{table_name}`;"
        cur.execute(SQL_Query)
        data = cur.fetchall()
        return data
    except mysql.connector.Error as err:
        print(f"❌ خطا در دریافت داده‌های جدول {table_name}: {err}")
        return []
    finally:
        cur.close()
        conn.close()


def add_data_in_file(table, database_data):
    """
    ذخیره داده‌های دیتابیس در فایل Pickle
    """
    try:
        os.makedirs('database_data', exist_ok=True)
        with open(os.path.join('database_data', f'{table}.pkl'), 'wb') as f:
            f.write(pickle.dumps(database_data))
        print(f"✅ داده‌های {table} ذخیره شد")
    except Exception as err:
        print(f"❌ خطا در ذخیره‌سازی {table}: {err}")


def read_database_data(table):
    """
    خواندن داده‌های ذخیره شده از فایل Pickle
    """
    try:
        with open(os.path.join('database_data', f'{table}.pkl'), 'rb') as f:
            read = f.read()
        return pickle.loads(read)
    except Exception as err:
        print(f"❌ خطا در خواندن {table}: {err}")
        return []


# ✅ اصلاح 4: بهبود تابع write_to_database با استفاده از Prepared Statements
def write_to_database(table, keys, values, db_config, database_name):
    """
    درج داده‌ها در دیتابیس
    اصلاح: استفاده از Prepared Statements برای امنیت
    """
    try:
        conn = mysql.connector.connect(**db_config, database=database_name)
        cur = conn.cursor()
        
        # ساخت رشته ستون‌ها
        columns_str = ", ".join([f"`{key}`" for key in keys])
        
        # ساخت placeholders
        placeholders = ", ".join(["%s"] * len(values))
        
        # کوئری نهایی
        sql = f"INSERT INTO `{table}` ({columns_str}) VALUES ({placeholders});"
        
        cur.execute(sql, values)
        conn.commit()
        print(f"✅ یک سطر به {table} اضافه شد")
    except mysql.connector.Error as err:
        print(f"❌ خطا در درج داده‌ها به {table}: {err}")
    finally:
        cur.close()
        conn.close()


# ✅ اصلاح 5: بهبود تابع اصلی
def main_write_data_to_file(db_config, database_name):
    """
    خواندن تمام داده‌های دیتابیس و ذخیره‌سازی در فایل
    اصلاح: اضافه کردن پارامترهای لازم
    """
    print("🔄 در حال خواندن داده‌های دیتابیس...")
    
    relations = get_relations(db_config, database_name)
    table_list = get_list_of_table(relations)
    
    # ذخیره لیست جداول
    add_data_in_file('main', table_list)
    
    # ذخیره داده‌های هر جدول
    for table in table_list:
        print(f"🔄 در حال پردازش جدول: {table}")
        data = get_table_data(table, db_config, database_name)
        add_data_in_file(table, data)
    
    print("✅ تمام داده‌ها ذخیره شدند")


def main_write_data(db_config, database_name):
    """
    خواندن داده‌های ذخیره شده و درج مجدد به دیتابیس
    ⚠️ اصلاح: این تابع ممکن است داده‌های تکراری درج کند
    بهتر است قبل از استفاده بررسی کنید
    """
    print("🔄 در حال درج داده‌ها به دیتابیس...")
    
    table_list = read_database_data('main')
    
    for table in table_list:
        data_rows = read_database_data(table)
        
        if not data_rows:
            print(f"⚠️ جدول {table} خالی است")
            continue
        
        # دریافت ستون‌ها از اولین سطر
        keys = list(data_rows[0].keys())
        
        for row in data_rows:
            # دریافت مقادیر
            values = tuple(row.values())
            
            # درج به دیتابیس
            write_to_database(table, keys, values, db_config, database_name)
    
    print("✅ تمام داده‌ها درج شدند")


# ✅ اصلاح 6: اضافه کردن شرط برای اجرای برنامه
if __name__ == "__main__":
    try:
        # ابتدا داده‌ها را خواندن و ذخیره کنید
        # main_write_data_to_file(db_config, database_name)
        
        # سپس برای درج مجدد، خط زیر را فعال کنید
        main_write_data(db_config, database_name)
    except NameError as err:
        print(f"❌ خطا: متغیرهای db_config یا database_name تعریف نشده‌اند")
        print(f"لطفاً آنها را در فایل config.py تعریف کنید")