import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_mainan"
)

cursor = database.cursor()
sql ="INSERT INTO customer_mainan (nama, deskripsi) VALUES (%s, %s)"
val = ("Remote Controller", "Jl.k")
cursor.execute(sql, val)

database.commit()
print("Data berhasil ditambahkan")