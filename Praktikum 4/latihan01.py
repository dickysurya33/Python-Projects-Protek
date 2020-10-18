import math
# waktu sewa
awal1 = 6
awal2 = 0
akhir1 = 23
akhir2 = 50

# tarif sewa
tarif_awal = 200000
tarif_lanjutan = 10000
tarif_menit = 10000/60

# penghitungan waktu sewa
waktu_sewa = math.floor(akhir1 - awal1 + (akhir2/60) - (awal2/60))

# penghitungan total sewa
print("Biaya Sewa Anda Adalah = Rp.",
      (waktu_sewa - 12)*tarif_lanjutan + tarif_awal)
