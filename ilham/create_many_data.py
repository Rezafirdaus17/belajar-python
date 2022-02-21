import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_garam"
)

cursor = database.cursor()
sql = "INSERT INTO rokok (nama, deskripsi) VALUES (%s, %s)"
data = [
    ("Djarum Super", 18000),
    ("Esse", 28000),
    ("Marlboro Filter", 32000),
    ("Berry Pop", 22000),
]

for val in data:
    cursor.execute(sql, val)
    database.commit()

print(cursor.rowcount, "Data Telah Ditambahkan")
print("{} data berhasil ditambahkan". format(len(data)))