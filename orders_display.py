import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="store_db"
)
cursor = connection.cursor()
sql="select * from orders"
cursor.execute(sql)
result=cursor.fetchall()
for row in result:
    print(row)
connection.close()