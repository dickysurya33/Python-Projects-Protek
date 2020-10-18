import math
# jarak
AB = 125
BC = 256

# kecepatan
kecepatan_AB = 62
kecepatan_BC = 70

# penghitungan waktu
waktu_berangkat = 6
waktu_tempuh_AB = math.ceil(AB / kecepatan_AB*60)
waktu_tempuh_BC = math.ceil(BC / kecepatan_BC*60)
waktu_istirahat = 45
total_perjalanan = waktu_tempuh_AB + waktu_tempuh_BC + waktu_istirahat
total_waktu_ditempuh = (total_perjalanan//60)+waktu_berangkat
total_menit = total_perjalanan % 60

# estimasi waktu

print("Pak Amir berangkat dari kota A menuju kota B pukul 06.00 dan beristirahat di kota B 45 menit, maka")
print("Pak Amir sampai di kota C pukul",
      (total_waktu_ditempuh), ":", (total_menit))
