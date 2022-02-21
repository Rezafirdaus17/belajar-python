import mysql.connector


db      = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="toko_sembako"
)

cursor = db.cursor()
sql = "INSERT INTO nama_sembako (nama, harga) VALUES (%s, %s)"
val = [
    ("Beras 1 kilo", 15000),
    ("Beras 2 kilo", 30000),
    ("Beras 3 kilo", 45000),
    ("Beras 4 kilo", 60000),
    ("Beras 5 kilo", 75000),
    ("Beras 6 kilo", 85000),
    ("Beras 7 kilo", 100000),
    ]

for data in val:
    cursor.execute(sql, data)
    db.commit()

print('{} Data berhasil ditambahkan'.format(len(data)))