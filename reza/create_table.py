import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_mainan"
)

cursor = database.cursor()
sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), price INT)"
cursor.execute(sql)

print("Table customers berhasil dibuat")
