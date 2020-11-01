kode = int(input("Masukan Kode Karyawan     => "))
nama = str(input("Masukan Nama Karyawan     => "))
golongan = str(input("Masukan Golongan Karyawan => "))
if (golongan == 'A'):
    Gajipokok = 10000000
    potonganGaji = 2.5
elif (golongan == 'B'):
    Gajipokok = 8500000
    potonganGaji = 2.0
elif (golongan == 'C'):
    Gajipokok = 7000000
    potonganGaji = 1.5
elif (golongan == 'D'):
    Gajipokok = 5500000
    potonganGaji = 1.0
else:
    print("Golongan Gaji tidak ditemukan")
    exit()


totalpotong = Gajipokok * (potonganGaji / 100)

print("===================================================")
print("Masukkan Kode Karyawan     => ", kode)
print("Masukkan Nama Karyawan     => ", nama)
print("Masukkan Golongan Karyawan => ", golongan)
print("===================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("===================================================")
print("Nama Karyawan              =>", nama)
print("Golongan                   =>", golongan)
print("---------------------------------------------------")
print("Gaji Pokok                 => Rp.", Gajipokok)
print("Potongan Gaji", potonganGaji, "%        => Rp.", totalpotong)
print("===================================================")
print("Gaji bersih                => Rp.", (Gajipokok - totalpotong))
print("---------------------------------------------------")
