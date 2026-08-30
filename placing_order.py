
import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="store_db")
cursor = connection.cursor()
print("Placing an order")
print("Select product from the list")
sql = "SELECT product_id, product_name FROM products"
cursor.execute(sql)
products = cursor.fetchall()
for product in products:
    print(f" {product[1]}, Product ID: {product[0]}")
p_id = int(input("Enter product id: "))
quantity = int(input("Enter quantity: "))
if quantity <= 0:
    print("Quantity must be greater than zero.")
else:
    sql = "SELECT * FROM products WHERE product_id = %s"
    values = (p_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("Order placed successfully")
    else:
        print("Product not found.")