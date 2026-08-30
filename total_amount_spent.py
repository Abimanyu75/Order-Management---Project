import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="store_db"
)
cursor = connection.cursor()
sql="""select c.customer_id, c.customer_name, o.total_amount 
from customers c join orders o 
on c.customer_id=o.customer_id"""
cursor.execute(sql)
result=cursor.fetchall()
for row in result:
    print(row)
connection.close()