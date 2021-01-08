from datetime import*

file = open('data.txt', 'a+')
data = []

while True:
    kode = input('Masukkan Kode Member : ')
    nama = input('Masukkan Nama Member : ')
    judul = input('Masukkan Judul Buku  : ')
    sekarang = datetime.date(datetime.now())
    tenggat = sekarang + timedelta(days=7)
    utuh = (f"{kode.upper()} | {nama.capitalize()} | {judul.capitalize()} | {str(sekarang)} | {str(tenggat)}")
    data.append(utuh)
    pertanyaan = input('Ulangi lagi (y/t)    : ')
    if pertanyaan != 'y' :
        break


index = 0
for tulis in data:
    tulis = str(data[index])
    file.write(tulis)
    file.write('\n')
    index += 1

file.close()