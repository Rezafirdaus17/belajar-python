import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="toko_sembako"
)

cursor = db.cursor()
sql = """CREATE TABLE nama_sembako (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255),
  harga Varchar(255)
)
"""
cursor.execute(sql)

print("Table nama_sembako berhasil dibuat")