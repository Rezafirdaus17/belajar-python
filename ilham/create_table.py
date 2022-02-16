import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="toko_gudang_garam"
)

cursor = db.cursor()
sql = """CREATE TABLE rokok (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255),
  deskripsi Varchar(255)
)
"""
cursor.execute(sql)

print("Table rokok berhasil dibuat")