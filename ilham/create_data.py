import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_garam"
)

cursor = database.cursor()
sql = "INSERT INTO rokok (nama, deskripsi) VALUES (%s, %s)"
val = ("Sampoerna Mild", 20000)
cursor.execute(sql, val)

database.commit()
print('Data berhasil ditambahkan')