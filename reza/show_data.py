import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_mainan"
)

cursor = database.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

# ambil semua data
# result = cursor.fetchall()

# ambil satu data
# result = cursor.fetchone()

# ambil data berdasarkan index
# result = cursor.fetchmany(2)

result = cursor.fetchmany(5)

# print(result)

for data in result:
    # print(data)
    print("ID: ", data[0])
    print("Name: ", data[1])
    print("Address: ", data[2])
    print("Price: ", data[3])
    print("----------------------------------")
