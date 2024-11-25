import pymysql


db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '28340186',
    'db': 'wangbi01'
}

# create connection
conn = pymysql.connect(**db_config)

cur = conn.cursor()
print(cur)