import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

if db.is_connected():
    print('berhasil terhubung kedatabase')
else:
    print('tidak dapat terhubung')
    print('tambah mumet')




