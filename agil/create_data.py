import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_gula"
)

cursor = database.cursor()
sql = "INSERT INTO gula (name, deskripsi) VALUES (%s, %s)"
val = ("gulaaren", 20000)

cursor.execute(sql , val)

database.commit()
print("Data berhasil ditambahkan")