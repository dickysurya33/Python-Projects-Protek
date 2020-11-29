print('------------------------')
print('Program penghitung rata-rata')
print('------------------------')
jumlah_data = 0
banyak_data = 0
kondisi = True
while (kondisi == True):
    try:
        input_bilangan = int(input('Masukkan bilangan Anda '))
        jumlah_data += input_bilangan
        banyak_data += 1
        pertanyaan = str(input(
            'Apakah Anda ingin menambahkan bilangan kembali? (y/t) : '))
        if (pertanyaan != 'y'):
            kondisi = False
            print('Rata-rata adalah', + jumlah_data/banyak_data)
    except (ValueError):
        print('Input yang Anda masukkan tidak valid')
