#print('test');
#lesson 2

#print(nama)
#print(usia)
#print(sudah_menikah)

#print ('nama saya',nama,'usia', usia,'dan saya', sudah_menikah)

#lesson 3
#a,b,c = 1,2,'mantaps'
#a=100
#b=50
#c=2
#d=true
#print(a-b/c,d)

#lesson 3
#print(single_variable)
# (a,b,c)
#print(type(b))
#print(type(c))
#lesson 4
#angka = 120
#if angka > 150:
#    print('ini lebih besar')
#else:
#    print('ini lebih kecil')

#angka = 120
#if angka < 150:
#        print('ini lebih kecil')
#elif angka > 150:
#        print('ini lebih besar')
#else:
#        print('invalid')

#nilai = int(input('masukkan nilai anda :'))

#if nilai < 150:
    #print ('ini jelek',150)
#elif nilai > 150:
    #print ('ini lebih besar')
#else:
    #print ('invalid')

#nama_buah = (input('masukan nama buah:'))
#buah = ['jeruk','apel','mangga']

#if nama_buah not in buah:
    #print ('buah tidak ada')

#if nama_buah in buah:
   # print ('buah ada')

# nilai_a = int(input('masukan nilai 1 :'))
# nilai_b = int(input('masukan nilai 2 :'))
#
# pengurangan = nilai_a - nilai_b
# perkalian = nilai_a * nilai_b
# penambahan = nilai_a + nilai_b
# pembagian = nilai_a / nilai_b
# persen = perkalian/100
#
# print(nilai_a,'ditambah dengan',nilai_b,'sama dengan',penambahan)
# print(nilai_a,'dikurang dengan',nilai_b,'sama dengan',pengurangan)
# print(nilai_a,'dkalikan dengan',nilai_b,'sama dengan',perkalian)
# print(nilai_a,'dibagiin dengan',nilai_b,'sama dengan',pembagian)
# print(persen,'%')
# print('='*100)
# print('='*50)
#study kasus


#nama_barang = (input('masukkan nama barang :'))
#barang = ['beras','gula','minyak']
#harga =int['10000[0]','5000[1]','7500[2]']
#jumlah_uang
#if nama_barang in barang :
   #print ('stock ada')
#elif nama_barang not in barang :
   #print ('stock kosong')


#harga_barang = int(input('beras' = 10000, 'gula' = 5000, 'minyak'=7500)

pilihan = 'y'
while pilihan == 'y':
    print('''
**********************************************
**********************************************

AGIL DI UDUD DULU
Smoking Warung

==============================================
==============================================
1. Jarum Super           : Rp 21.000 sebungkus
2. Jarum Coklat          : Rp 17.000 sebungkus
3. Gudang Garam Merah    : Rp 15.000 sebungkus
4. Sampoerna Mild        : Rp 25.000 sebungkus
==============================================
==============================================
''')
    pesan       = str(input('masukkan No rokok       = '))
    jumlahpesan = int(input('masukkan jumlah pesanan = '))
    uangcash    = int(input('masukkan uang anda      = '))
    if pesan == '1':
        listnama = 'Jarum Super'
        harga = int(21000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 50:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
            kembalian  = int(uangcash - totalharga)
        else:
            diskon = (0)
            totalharga = int(harga + ppn)
            kembalian = int(uangcash - totalharga)
            kurang = int(totalharga - uangcash)
    elif pesan == '2':
        listnama = 'Jarum Coklat'
        harga = int(17000 * jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 50:
            diskon = int(harga * 0.2)
            totalharga = int(harga - diskon + ppn)
            kembalian = int(uangcash - totalharga)
        else:
            diskon = (0)
            totalharga = int(harga + ppn)
            kembalian = int(uangcash - totalharga)
    elif pesan == '3':
        listnama = 'Gudang Garam Merah'
        harga = int(15000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
        kembalian = int(uangcash - totalharga)
    elif pesan == '4':
        listnama = 'Sampoerna Mild'
        harga = int(20000 * jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga + ppn)
        kembalian = int(uangcash - totalharga)
    else:
        listnama = '-'
        harga = '-'
        ppn = '-'
        diskon = '-'
        totalharga = '-'
        uangcash = '-'
        kembalian = '-'
        pilihan = input('Warung Bangkrut, Pesan udud yg lainnya aja yaa Y/N =')

    print('--------------------------')
    print('Agil kang udud')
    print('--------------------------')
    print('Udud         :', listnama)
    print('Jumlah Pesan :', jumlahpesan)
    print('Harga        :', harga)
    print('Diskon       :', diskon)
    print('PPN          :', ppn)
    print('--------------------------')
    print('Jumlah Bayar :', totalharga)
    if uangcash < totalharga:
        print ('maaf uang anda kurang')
    elif uangcash > totalharga:
        print('Kembalian    :', kembalian)
    print('--------------------------')
    pilihan = input('Mau pesan lagi ?? Y/N =')
