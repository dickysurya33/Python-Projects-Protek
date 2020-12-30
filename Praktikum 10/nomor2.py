data_nim = []
data_nama = []
data_alamat = []
status = 'y'
buka = open('nomor2.txt','a+')

while (status == 'y'):
    nim = input(str('Masukkan NIM Anda : '))
    nama = input(str('Masukkan Nama Anda : '))
    alamat = input(str('Masukkan Alamat Anda : '))
    data_nim.append(nim)
    data_nama.append(nama)
    data_alamat.append(alamat)
    konfirmasi = input('Apakah Anda ingin memasukkan data lagi? y/t : ')
    if konfirmasi != 'y':
        status = 't'

for i in range(len(data_nim)):
    daftar_nim = data_nim[i]
    daftar_nama = data_nama[i]
    daftar_alamat = data_alamat[i]
    a = f'{daftar_nim} | {daftar_nama} | {daftar_alamat}'
    buka.write(a + '\n')

print(r'Data Anda disimpan di "nomor2.txt" pada folder ini')
    
   
    





