import mysql.connector


db      = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="toko_sembako"
)

cursor = db.cursor()
sql = "INSERT INTO nama_sembako (nama, harga) VALUES (%s, %s)"
val = ("Beras 1 kilo", 15000)
cursor.execute(sql, val)

db.commit()
print('Data berhasil ditambahkan')