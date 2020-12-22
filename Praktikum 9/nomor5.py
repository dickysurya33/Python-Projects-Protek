nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('=' * 60)
print("NIM".ljust(17), "NAMA".ljust(15), "N. MID".rjust(8), "N. UAS".rjust(16))
print("-"*60)
for tabel in nilai:
    print(tabel['nim'].ljust(17),
        tabel['nama'].ljust(15), 
        str(tabel['mid']).rjust(8), 
        str(tabel['uas']).rjust(16))
print('=' * 60)