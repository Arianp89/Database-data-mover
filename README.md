# 🗄️ Database Manager - Improved Version

**🇬🇧 English Version | [🇮🇷 مسنتدات فارسی](README.FA.md)**

![Status](https://img.shields.io/badge/status-production%20ready-brightgreen)
![Version](https://img.shields.io/badge/version-2.0-blue)
![Language](https://img.shields.io/badge/languages-EN%2FFA-orange)

---

## 📖 Overview

A professional-grade **MySQL Database Manager** with bilingual support (English & Persian). This tool helps you easily export database data to files and import it back with a user-friendly interface.

### ✨ Key Features

- ✅ **Bilingual Interface** - Full English and Persian support
- ✅ **User-Friendly Input** - Clean, formatted prompts with defaults
- ✅ **Intelligent Export** - Analyze and save all database tables
- ✅ **Safe Import** - Re-insert data with proper error handling
- ✅ **Security** - Protected against SQL Injection attacks
- ✅ **Professional UI** - Beautiful console formatting
- ✅ **Complete Error Handling** - Comprehensive exception management
- ✅ **Object-Oriented** - Clean, maintainable code structure

---

## 🚀 Quick Start

### 1. Installation

```bash
# Install required package
pip install mysql-connector-python
```

### 2. Run the Program

```bash
python information-database-improved.py
```

### 3. Follow the Prompts

```
Choose language (EN/FA) [default: EN]: EN

============================================================
   DATABASE CONFIGURATION
============================================================
Enter database host (default: localhost): 
Enter database user (default: root): 
Enter database password: your_password
Enter database name: your_database

✅ Configuration complete!

============================================================
   MAIN MENU
============================================================
  1️⃣  Export database data to files
  2️⃣  Import data from files to database
  3️⃣  Exit

Select an option (1-3): 1
```

---

## 📋 Program Flow

```
START
  ↓
  Choose Language (EN/FA)
  ↓
  Enter Database Configuration
  ├─ Host (default: localhost)
  ├─ User (default: root)
  ├─ Password
  └─ Database Name
  ↓
  Main Menu Loop
  ├─ Option 1: Export Data
  │  ├─ Connect to Database
  │  ├─ Get Table Relationships
  │  ├─ Fetch Table Data
  │  └─ Save to Pickle Files
  │
  ├─ Option 2: Import Data
  │  ├─ Read Pickle Files
  │  ├─ Connect to Database
  │  └─ Insert Data Back
  │
  └─ Option 3: Exit
  ↓
END
```

---

## 🎯 Usage Examples

### Example 1: Export Database Data

```python
$ python information-database-improved.py

Choose language (EN/FA) [default: EN]: EN

# Follow the prompts and select option 1
# The program will:
# 1. Connect to your database
# 2. Fetch all tables and relationships
# 3. Download all data
# 4. Save to database_data/ folder
```

**Output:**
```
============================================================
   MAIN MENU
============================================================
  1️⃣  Export database data to files
  2️⃣  Import data from files to database
  3️⃣  Exit

Select an option (1-3): 1

============================================================
🔄 Reading database data...
============================================================

🔄 Processing table: users
✅ Data for users saved successfully
🔄 Processing table: products
✅ Data for products saved successfully
🔄 Processing table: orders
✅ Data for orders saved successfully

============================================================
✅ All data has been saved
============================================================
```

### Example 2: Import Data Back

```python
# Select option 2 from the menu
# The program will read saved data and insert it back
```

**Output:**
```
============================================================
🔄 Inserting data into database...
============================================================

✅ One row added to users
✅ One row added to users
✅ One row added to products
✅ One row added to products
✅ One row added to orders

============================================================
✅ All data inserted successfully
============================================================
```

---

## 🏗️ Code Structure

### Class: `DatabaseManager`

```python
class DatabaseManager:
    def __init__(self, db_config, database_name)
    def set_language(self, lang)
    def get_relations(self) -> List[Dict]
    def get_list_of_table(self, relations) -> List[str]
    def get_table_data(self, table_name) -> List[Dict]
    def add_data_in_file(self, table, database_data) -> bool
    def read_database_data(self, table) -> Any
    def write_to_database(self, table, keys, values) -> bool
    def export_to_file(self) -> bool
    def import_from_file(self) -> bool
```

### Helper Functions

```python
def get_database_config(language) -> Tuple[Dict, str]
def display_menu(language) -> str
def main()
```

---

## 📁 File Structure

After running the program, you'll see:

```
.
├── information-database-improved.py    # Main program
├── README.md                           # English documentation
├── README_IMPROVED_FA.md              # Persian documentation
│
└── database_data/                      # Data directory (created automatically)
    ├── main.pkl                        # Table list
    ├── users.pkl                       # Users table data
    ├── products.pkl                    # Products table data
    ├── orders.pkl                      # Orders table data
    └── ...                             # Other tables
```

---

## 🔐 Security Features

### 1. SQL Injection Protection
```python
# ✅ Table names are validated
if not table_name.isalnum() and '_' not in table_name:
    return []

# ✅ Using backticks for identifiers
SQL_Query = f"SELECT * FROM `{table_name}`;"

# ✅ Using Prepared Statements for values
sql = f"INSERT INTO `{table}` ({columns_str}) VALUES ({placeholders});"
cur.execute(sql, values)  # Values are safely parameterized
```

### 2. Error Handling
```python
try:
    # Database operations
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cur.close()
    conn.close()
```

### 3. Input Validation
```python
# Database configuration with defaults
host = input(prompt).strip() or "localhost"
user = input(prompt).strip() or "root"

# Menu option validation
while True:
    choice = input(prompt).strip()
    if choice in ['1', '2', '3']:
        break
```

---

## 🌍 Bilingual Support

The program supports both **English** and **Persian** with a comprehensive message system:

### Languages Supported
- 🇬🇧 **English** - Complete interface and messages
- 🇮🇷 **Persian (فارسی)** - تمام رابط و پیام‌ها

### Switching Languages

```bash
Choose language (EN/FA) [default: EN]: FA
```

Or in the code:

```python
manager = DatabaseManager(db_config, database_name)
manager.set_language("FA")  # Switch to Persian
```

---

## 📊 Database Compatibility

### ✅ Compatible With
- MySQL 5.7+
- MySQL 8.0+
- MariaDB 10.1+
- Amazon RDS MySQL
- Google Cloud SQL
- Azure Database for MySQL

### ✅ Works With
- Any number of tables
- Large datasets (with pagination)
- Foreign key relationships
- Complex schemas

---

## ⚠️ Important Notes

### 1. Backup First
```bash
# Always backup your database before importing
mysqldump -u root -p database_name > backup.sql
```

### 2. Duplicate Data Risk
```
⚠️  WARNING: Importing data may create duplicates
    
Solution: 
1. Clear the tables first (TRUNCATE TABLE)
2. Or use REPLACE INTO instead of INSERT
3. Check for primary key conflicts
```

### 3. Foreign Key Constraints
```
⚠️  If your database has foreign keys:

1. Disable foreign key checks during import
2. Import parent tables first
3. Then import child tables
```

### 4. Large Databases
```
⚠️  For very large databases:

Consider:
- Using pagination
- Splitting import into batches
- Using direct SQL dumps (mysqldump)
```

---

## 🐛 Troubleshooting

### Error: `Access denied for user 'root'@'localhost'`

**Problem:** Wrong password or user

**Solution:**
```bash
# Check MySQL credentials
mysql -u root -p -h localhost

# Verify database exists
SHOW DATABASES;
```

### Error: `Unknown database 'my_database'`

**Problem:** Database doesn't exist

**Solution:**
```bash
# Create database
mysql -u root -p
CREATE DATABASE my_database;
```

### Error: `No module named 'mysql'`

**Problem:** mysql-connector-python not installed

**Solution:**
```bash
pip install mysql-connector-python
```

### Error: `Pickle file not found`

**Problem:** Database data not exported yet

**Solution:**
```bash
# First run: Select option 1 (Export)
# Then run: Select option 2 (Import)
```

### Error: `Duplicate entry`

**Problem:** Data already exists in database

**Solution:**
```bash
# Clear tables before importing
TRUNCATE TABLE table_name;

# Or delete specific data
DELETE FROM table_name WHERE id > 0;
```

---

## 📊 Performance Tips

### Optimize Export
```python
# Large tables - use batching
for i in range(0, len(data), 1000):
    batch = data[i:i+1000]
    # process batch
```

### Optimize Import
```python
# Use transactions for multiple rows
SET autocommit=0;
BEGIN;
-- INSERT statements
COMMIT;
```

### Monitor Progress
```bash
# Check file sizes
ls -lh database_data/

# Check row counts
SELECT COUNT(*) FROM table_name;
```

---

## 📚 Advanced Usage

### Programmatic Usage

```python
from information_database_improved import DatabaseManager

# Initialize
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password'
}
manager = DatabaseManager(db_config, 'my_database')
manager.set_language('EN')

# Export data
manager.export_to_file()

# Import data
manager.import_from_file()
```

### Custom Message System

```python
# Get localized message
message = manager._get_message("data_saved", lang="EN")
print(message.format("users"))  # Output: ✅ Data for users saved successfully
```

### Schedule Regular Backups

```python
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(manager.export_to_file, 'cron', hour=2)  # Daily at 2 AM
scheduler.start()
```

---

## 🔄 Data Backup Workflow

```
Scenario: Migrate database to new server

1. Export from old database
   python information-database-improved.py
   Option: 1 (Export)

2. Transfer database_data/ folder to new server

3. Import to new database
   python information-database-improved.py
   Option: 2 (Import)

Result: ✅ All data safely migrated
```

---

## 📈 Comparison: Old vs New

| Feature | Old Version | New Version |
|---------|------------|-------------|
| Language Support | Persian only | English + Persian |
| Input Handling | Basic | Advanced with defaults |
| Error Messages | Generic | Specific and localized |
| Code Structure | Procedural | Object-Oriented |
| User Interface | Plain text | Formatted with borders |
| Configuration | Hard-coded | Interactive |
| Menu System | Simple | Robust with validation |
| Documentation | Minimal | Comprehensive |

---

## 🎓 Learning Resources

### Understanding the Code

```python
# 1. Message System
manager._get_message(key, lang)

# 2. Database Connection
mysql.connector.connect(**db_config, database=database_name)

# 3. Data Serialization
pickle.dumps(data)  # Serialize
pickle.loads(data)  # Deserialize

# 4. File Operations
with open(path, 'rb') as f:
    data = f.read()
```

### SQL Concepts Used

- Foreign Keys
- Table Relationships
- Information Schema
- Data Types
- Insert/Select Statements

---

## 🌟 Best Practices

1. **Always backup before import**
2. **Test with small dataset first**
3. **Monitor disk space for large exports**
4. **Use strong passwords**
5. **Keep database credentials secure**
6. **Log important operations**
7. **Version your database backups**
8. **Document your data schema**

---

## 📞 Support & Help

### Getting Help

- Check the Troubleshooting section
- Read the code comments
- Review the Persian version: [README_IMPROVED_FA.md](./README_IMPROVED_FA.md)
- Check MySQL documentation

### Report Issues

- Describe the problem clearly
- Include error messages
- Provide database version
- Share sample of your data structure

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🎉 Features Summary

```
✅ Bilingual (EN/FA)
✅ User-Friendly Input
✅ Professional UI
✅ Security Hardened
✅ Error Handling
✅ Object-Oriented
✅ Type Hints
✅ Comprehensive Docs
✅ Production Ready
✅ Easy to Extend
```

---

**Last Updated:** June 14, 2026

**Created with ❤️ for Database Professionals**

---

## 🚀 Next Steps

1. **Install**: `pip install mysql-connector-python`
2. **Run**: `python information-database-improved.py`
3. **Choose Language**: EN or FA
4. **Enter Configuration**: Database credentials
5. **Select Operation**: Export or Import
6. **Monitor Progress**: Check the output messages
7. **Verify Results**: Check `database_data/` folder

---

**Happy Database Management! 🗄️✨**
