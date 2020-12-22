mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("="*77)
print("NIM".ljust(13),"NAMA MAHASISWA".ljust(20), "TGL LAHIR".rjust(15), "TEMPAT LAHIR".rjust(25))
print("-"*77)

for tabel in mhs:
    kolom = tabel.split(":")
    lahir = kolom[2].split("-")
    print(kolom[0].ljust(13), 
        kolom[1].ljust(20), 
        (str(lahir[2])+"/"+str(lahir[1])+"/"+str(lahir[0])).rjust(15), 
        kolom[3].rjust(25))
        
print("="*77)