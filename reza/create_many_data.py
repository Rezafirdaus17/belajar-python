import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko_mainan"
)

cursor = database.cursor()
sql = "INSERT INTO customers (name, address, price) VALUES (%s, %s, %s)"
data = [
    ("Reza", "Jl. Asda", 100000),
    ("Asd", "Jl. FAsd", 100000),
    ("RezDa", "Jl. Fafs", 100000),
    ("Fas", "Jl. VAs", 100000),
    ("qDqw", "Jl. asd", 100000),
    ("Cacs", "Jl. Rq", 100000),
    ("RQsq", "Jl. aq", 100000),
    ("Fasd", "Jl. FAr", 100000),
    ("Reza", "Jl. Asda", 100000),
    ("Asd", "Jl. FAsd", 100000),
    ("RezDa", "Jl. Fafs", 100000),
    ("Fas", "Jl. VAs", 100000),
    ("qDqw", "Jl. asd", 100000),
    ("Cacs", "Jl. Rq", 100000),
    ("RQsq", "Jl. aq", 100000),
    ("Fasd", "Jl. FAr", 100000),
]

for val in data:
    cursor.execute(sql, val)
    database.commit()

print("{} data berhasil ditambahkan".format(len(data)))
