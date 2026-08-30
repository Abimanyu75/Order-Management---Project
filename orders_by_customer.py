import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="store_db"
)
cursor = connection.cursor()
Name = input("Enter customer name: ")
sql="""select c.customer_id, c.customer_name, o.order_id,
p.product_name,ot.quantity, o.total_amount 
from customers c join orders o
on c.customer_id=o.customer_id 
join order_items ot 
on ot.order_id=o.order_id 
join products p on p.product_id=ot.product_id 
where c.customer_name=%s"""
values=(Name,)
cursor.execute(sql,values)
result=cursor.fetchall()
for row in result:
    print(row)
connection.close()