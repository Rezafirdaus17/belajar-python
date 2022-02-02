import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

db_created = 'CREATE DATABASE toko_gudang_garam'

cursor = db.cursor()
cursor.execute(db_created)

print('db berhasil dibuat')