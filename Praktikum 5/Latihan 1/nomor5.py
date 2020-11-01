kode = int(input("Masukan Kode Karyawan     => "))
Nama_Karyawan = str(input("Masukan Nama Karyawan     => "))
golKar = str(input("Masukan Golongan Karyawan => "))
married = int(
    input("Masukan status anda (1. sudah menikah / 2. belum): (Tekan 1/2) "))

if(married == 1):
    statusnya = "sudah menikah"
    anak = int(input("jumlah anak :"))
else:
    statusnya = "belum"

if (golKar == 'A'):
    Gaji = 10000000
    potonganGaji = 2.5
elif (golKar == 'B'):
    Gaji = 8500000
    potonganGaji = 2.0
elif (golKar == 'C'):
    Gaji = 7000000
    potonganGaji = 1.5
elif (golKar == 'D'):
    Gaji = 5500000
    potonganGaji = 1.0
else:
    print("Golongan Gaji tidak ditemukan")
    exit()

# Tunjangan Gaji Menikah
if (statusnya == "sudah menikah"):
    Istri = Gaji * 10/100
    Anak = anak * Gaji * 5/100

# Gaji kotor dan bersih
if (statusnya == "sudah menikah"):
    gKotor = Gaji + Istri + Anak
elif (statusnya == "belum"):
    gKotor = Gaji

hitung = Gaji * (potonganGaji/100)


print("Masukkan Kode Karyawan     => ", kode)
print("Masukkan Nama Karyawan     => ", Nama_Karyawan)
print("Masukkan Golongan Karyawan => ", golKar)
print("Status                     => ", statusnya)
if(statusnya == "sudah menikah"):
    print("jumlah anak             =>", anak)
print("===================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------------------")
print("Nama Karyawan              =>", Nama_Karyawan)
print("Golongan                   =>", golKar)
print("Gaji Pokok                 =>Rp.", int(Gaji))
if(statusnya == "sudah menikah"):
    print("Tunjangan Istri         =>Rp.", int(Istri))
    print("Tunjangan anak          =>Rp.", int(Anak))
print("---------------------------------------------------")
print("Gaji kotor                 => Rp {0}".format(gKotor))
print("Potongan                   =>", potonganGaji, "%", hitung)
print("---------------------------------------------------")
print("Gaji Bersih                => Rp {0}".format(gKotor - hitung))
