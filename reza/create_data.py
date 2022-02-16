import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_mainan"
)

cursor = database.cursor()
sql = "INSERT INTO customers (name, address, price) VALUES (%s, %s, %s)"
val = ("Reza", "Jl. Raya", 20000)
cursor.execute(sql, val)

database.commit()
print('Data berhasil ditambahkan')
