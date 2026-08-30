import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="store_db"
)
cursor = connection.cursor()
print("Enter the product id and quantity to place an order")
p_id = int(input("Enter product id: "))
quantity = int(input("Enter quantity: "))
sql = "SELECT stock FROM products WHERE product_id = %s"
values = (p_id,)
cursor.execute(sql, values)
result = cursor.fetchone()
if result:
    available_stock = result[0]
    if quantity <= available_stock:
        print("Order placed successfully.")
        new_stock = available_stock - quantity
        sql = "UPDATE products SET stock = %s WHERE product_id = %s"
        values = (new_stock, p_id)
        cursor.execute(sql, values)
        connection.commit()
    else:
        print("Insufficient stock.")
else:
    print("Product not found.")