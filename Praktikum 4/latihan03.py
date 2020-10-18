import time
import datetime
# jarak tempuh
jarak = 795

# asumssi bbm
asumsi_bensin = 12

# penghitungan bensin
bensin_dibutuhkan = jarak / asumsi_bensin

# total bensin yang dibutuhkan
print("bensin yang dibutuhkan(lt)= ", (bensin_dibutuhkan))
time.sleep(2)
print("jika bensin awal sudah penuh")
time.sleep(2)

# penghitungan pengisian
banyakisi = bensin_dibutuhkan//50
print("banyak isi bensin=", ((banyakisi)))
