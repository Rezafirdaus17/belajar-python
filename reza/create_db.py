import mysql.connector


database = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

db_created = "CREATE DATABASE toko_mainan"

cursor = database.cursor()
cursor.execute(db_created)

print("db berhasil dibuat")
