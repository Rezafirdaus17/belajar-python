import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_gula"
)

cursor = database.cursor()
sql = "SELECT * FROM gula"
cursor.execute(sql)
#
# result = cursor.fetchall() # mengambil semua data

result = cursor.fetchmany(2) # mengambil sesuai kebutuhan

# result = cursor.fetchon() # mengambil satu data

# for data in result(0:2) # mengambil sesuai kebutuhan

for data in result:
    # print(data)
    print("ID: ", data[0])
    print("Name: ", data[1])
    print("Address: ", data[2])
    print("------------------")