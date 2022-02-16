import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if database.is_connected():
    print("Codingan sudah terhubung ke server xampp")
else:
    print("koneksi gagal")
