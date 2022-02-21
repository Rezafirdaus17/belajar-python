import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_gula"
)
cursor = database.cursor()
sql = "INSERT INTO gula (name, deskripsi) VALUES (%s, %s)"
data = [
    ("gula merah", 10000),
    ("gula cair", 15000),
    ("gula pasir", 13000)
]

for val in data:
    cursor.execute(sql, val)
    database.commit()

print(cursor.rowcount, "Data berhasil ditambahkan")



