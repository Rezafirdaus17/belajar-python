import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

db_create = "CREATE DATABASE toko_gudang_gula"

cursor = db.cursor()
cursor.execute(db_create)

print("db berhasil dibuat")