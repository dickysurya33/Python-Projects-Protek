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

y = input('Masukkan Tahun : ')
m = input('Masukkan Bulan : ')
d = input('Masukkan Tanggal : ')

print(diffDate(f'{y}-{m}-{d}'))

