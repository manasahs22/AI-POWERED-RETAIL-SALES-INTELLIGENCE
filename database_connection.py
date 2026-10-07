import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPassword",
    database="retail_sales"
)

if connection.is_connected():
    print("MySQL Connected Successfully!")

connection.close()