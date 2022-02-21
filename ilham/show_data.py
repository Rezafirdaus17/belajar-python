import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_garam"
)

cursor = database.cursor()
sql = "SELECT * FROM rokok"
cursor.execute(sql)


# ambil semua data
result = cursor.fetchall()

# ambil satu data
# result = cursor.fetchone()

# ambil data berdasarkan index
# result = cursor.fetchmany(5)

for data in result:
    print(data)
