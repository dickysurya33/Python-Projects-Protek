nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('=' * 98)
print("NIM".ljust(17), "NAMA".ljust(15), "N. MID".rjust(8), "N. UAS".rjust(16), "N. AKHIR".rjust(18), "STATUS".rjust(18))
print("-"*98)


for tabel in nilai:
    nilai_akhir = int((tabel['mid'] + 2 * tabel['uas'])/3)
    kelulusan=''
    if nilai_akhir >= 60 :
        kelulusan = 'LULUS'
    else:
        kelulusan = 'TIDAK LULUS'
    print(tabel['nim'].ljust(17),
        tabel['nama'].ljust(15), 
        str(tabel['mid']).rjust(8), 
        str(tabel['uas']).rjust(16),
        str(nilai_akhir).rjust(18),
        str(kelulusan).rjust(18))
print('=' * 98)