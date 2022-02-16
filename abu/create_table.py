import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_mainan"
)

cursor = database.cursor()
sql = "CREATE TABLE customer_mainan (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(255), deskripsi VARCHAR(255))"
cursor.execute(sql)

print("Table mainan berhasil dibuat")
