import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_gudang_gula"
)

cursor = database.cursor()
sql = "INSERT INTO gula (name, deskripsi) VALUES (%s, %s)"
val = ("gulaaren", 20000)

cursor.execute(sql, val)

database.commit()
print("Data berhasil ditambahkan")

sql=int(input("Masukan Jumlah Jam Kerja jk : "))
val=int(input("Masukan Jumlah jam Lembur jl : "))

jk=sql*15000
jl=val*10000

um=sql*10000

print("jumlah Jam kerja :",jk)
print("jumlah Jam Lembur :",jl)
print("jumlah Uang Makan :",um)
print("Gaji Anda bulan ini :",jk+jl+um)

