from datetime import *



def diffDate(x):
    pisah = x.split('-')
    tahun = int(pisah[0])
    bulan = int(pisah[1])
    hari = int(pisah[2])
    sekarang = datetime.now()
    diminta = datetime(tahun,bulan,hari)
    selisih = sekarang - diminta
    return selisih


file = open("data.txt", "r")

baca_file = file.readlines()
kode = input("Masukkan Kode Member : ")

for i in range(len(baca_file)) :
    if(kode in baca_file[i]) :
        splitted = baca_file[i].split('|')
        status = True
        break

    else :
        status = False
        continue


if(status == True) :
    
    print("\nData Peminjaman Buku")
    print("Kode Member : ", splitted[0])
    print("Nama Member : ", splitted[1])
    print("Judul Buku : ", splitted[2])
    print("Tanggal Mulai Peminjaman : ", splitted[3])
    print("Tanggal Maks Peminjaman : ", splitted[4])
    print("Tanggal Pengembalian : ", datetime.date(datetime.now()))

    waktu = datetime.now()

    tahun_sekarang = waktu.year
    bulan_sekarang = waktu.month
    hari_Sekarang = waktu.day

    terlambat = diffDate(f'{tahun_sekarang} - {bulan_sekarang} - {hari_Sekarang}')
    denda = 2000 * (terlambat)

    if(terlambat == 0) :
        print("Terlambat : 0 hari")
        print("Denda : 0")
        
    else :
        print("Terlambat : ", (terlambat))
        print("Denda : ", denda)
    