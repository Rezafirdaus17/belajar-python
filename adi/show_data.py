import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="toko_sembako"
)

cursor = db.cursor()
sql = "select * from nama_sembako"
cursor.execute(sql)

result = cursor.fetchmany(2)

for data in result: #[0:2]:
    #print(data)
    print ('Id    :', data[0])
    print ('Nama  :', data[1])
    print ('Harga :', data[2])
    print ('=====================')

