import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="store_db"
)
cursor = connection.cursor()
sql="select sum(total_amount) from orders"
cursor.execute(sql)
result = cursor.fetchone()
print("Total order amount :", result[0])