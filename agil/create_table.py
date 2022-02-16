import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_gula"
)

cursor = database.cursor()
sql = """CREATE TABLE gula (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  deskripsi Varchar(255)
)
"""
cursor.execute(sql)

print("Table gula berhasil dibuat")