# # Leason 1
# print ('Saya Ganteng Maksimal')
#
# Leason 2
# x = 'Saya'
# y = 'Ganteng Banget'
# z = True
#
# print (x)
# print (y)
# print (z)
# print(x,y,z)

# Leason 3

# single_variable = 'ini single variable'
# a, b, c = (123, 'ini multiple', True)
# a = 2
# b = 3
#
# print(a*b+b)

# print(single_variable)
# print(a,b,c)
# print(a)
# print(b)
# print(c)
# print(type(a),type(b),type(c))
# print(type(a))
# print(type(b))
# print(type(c))

# Leason 4 (if elif else)
# angka = 120
# if angka < 150:
#      print('ini lebih kecil')
# elif angka > 150:
#      print('ini lebih besar')
# else:
#     print('invalid')
#
# angka = 120
# if angka <= 150:
#      print(angka)
# elif angka > 150:
#      print('ini lebih besar')
# else:
#     print('invalid')

# Leason 5
# nilai = int(input('Masukkan nilai anda : '))
# if nilai < 150:
#      print(nilai,'lebih kecil dari 150')
# elif nilai > 150:
#      print(nilai,'lebih besar dari 150')
# else:
#     print('invalid')

# nilai_a = int(input('Masukkan nilai pertama : '))
# nilai_b = int(input('Masukkan nilai kedua : '))
#
# if nilai_a < nilai_b:
#      print(nilai_a,'lebih kecil dari',nilai_b)
# elif nilai_a > nilai_b:
#      print(nilai_a,'lebih besar dari',nilai_b)
# else:
#     print('invalid')

# nama_buah = str(input('Masukkan nama buah : '))
# buah = ['jeruk', 'rambutan', 'melon']
# if nama_buah not in buah:
#     print('buah tidak ada')
#
# if nama_buah in buah:
#     print('buah ada')


# nilai_a = int(input('Masukkan nilai 1 : '))
# nilai_b = int(input('Masukkan nilai 2 : '))
#
# penjumlahan = nilai_a + nilai_b
# pengurangan = nilai_a - nilai_b
# perkalian = nilai_a * nilai_b
# pembagian = nilai_a / nilai_b
# persen = perkalian / 100
#
# print(nilai_a, 'ditambah', nilai_b, 'sama dengan', penjumlahan)
# print(nilai_a, 'dikurang', nilai_b, 'sama dengan', pengurangan)
# print(nilai_a, 'dikali', nilai_b, 'sama dengan', perkalian)
# print(nilai_a, 'dibagi', nilai_b, 'sama dengan', pembagian)
# print(persen, '%')

# Study Kasus

print('=' * 20, 'TOKO GUDANG GARAM', '=' * 20)

print('List Nama Rokok Yang Tersedia')
print('1. Sampoerna Mild : Rp 26000')
print('2. Gudang Garam Filter : Rp 18000')
print('3. DJI SAM SOE : Rp 22000')
print('4. Surya Pro : Rp 27000')
print('5. ESSE : Rp 28000')

print('=' * 40)

list_rokok = str(input('Masukkan nomor sesuai list rokok yang tersedia : '))
jrokok = int(input('Masukkan jumlah rokok : '))
juang = int(input('Masukkan jumlah uang anda : '))

if list_rokok == '1':
    nama_rokok = 'sampoerna'
    harga = (26000 * jrokok)
    kembalian = (juang - harga)
    total_harga = (harga)

elif list_rokok == '2':
    nama_rokok = 'filter'
    harga = (18000 * jrokok)
    kembalian = (juang - harga)
    total_harga = (harga)

elif list_rokok == '3':
    nama_rokok = 'djisamsoe'
    harga = (22000 * jrokok)
    kembalian = (juang - harga)
    total_harga = (harga)

elif list_rokok == '4':
    nama_rokok = 'surya'
    harga = (27000 * jrokok)
    kembalian = (juang - harga)
    total_harga = (harga)

elif list_rokok == '5':
    nama_rokok = 'esse'
    harga = (28000 * jrokok)
    kembalian = (juang - harga)
    total_harga = (harga)

else:
    list_rokok = input('maaf rokok yang ada cari tidak tersedia')


print('=' * 30)

print('Nama rokok :', nama_rokok)
print('Jumlah Pesanan :', jrokok, 'bungkus')
print('Harga :', harga)

print('=' * 20)

print('Total :', total_harga)
print('Tunai :', juang)
if juang < total_harga:
    print('maaf uang anda kurang')
elif juang > total_harga:
    print('Kembalian :', kembalian)
print('=' * 30)
