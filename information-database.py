import mysql.connector



database_name = input('enter your database_name:')
host = input('enter database host address:')
user = input('enter database user:')
password = input('enter database password:')
db_config = {'host':host , 'user':user , 'password':password}





def get_relations (db_config , database_name):
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
    conn.close()
    cur.close()
    return relations



def check_foreign_key(relations):
    datas = dict()
    for rel in relations:
        if rel['REFERENCED_TABLE_NAME'] != None:
            if rel['REFERENCED_TABLE_NAME'] not in datas:
                datas[rel['TABLE_NAME']] = 1
            else:
                datas[rel['TABLE_NAME']] += 1

        elif rel['REFERENCED_TABLE_NAME'] == None:
            if rel['REFERENCED_TABLE_NAME'] not in datas:
                datas[rel['TABLE_NAME']] = 1
            else:
                datas[rel['TABLE_NAME']] += 1
    data=dict()
    for table_name, num in datas.items():
        if num not in data:
            data[num]=[table_name]
        elif num in data:
            data[num].append(table_name)
    table_list = []
    for i in data:
        for ii in data.get(i):   
            table_list.append(ii)

    return table_list  



def get_table_data(table_name):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = f"SELECT * FROM {table_name} ;"
    cur.execute(SQL_Query)
    data = cur.fetchall()    
    cur.close()
    conn.close()
    return data
