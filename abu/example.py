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