pertanyaan = 'y'
sayur = ['bayam', 'kangkung', 'wortel', 'selada']

while (pertanyaan == 'y'):
    print('========MENU========')
    print('A. Tambah data sayur')
    print('B. Hapus data sayur')
    print('C. Tampilkan data sayur\n')

    pilihan = str(input('Silakan pilih menu : '))
    if (pilihan.lower() == 'a'):
        tambah_sayur = str(
            input('Masukkan sayur yang ingin Anda tambahkan : '))
        sayur.append(tambah_sayur)
    elif (pilihan.lower() == 'b'):
        hapus_sayur = input('Masukkan nama sayur yang ingin Anda hapus : ')
        try:
            sayur.remove(hapus_sayur)
            print(hapus_sayur, 'berhasil dihapus')
        except (ValueError):
            print(hapus_sayur, 'Tidak ada dalam daftar sayur')
    elif (pilihan.lower() == 'c'):
        print('Daftar sayur adalah : ',  end='')
        for i in (sayur):
            print(i, '', end='')
        print('\n')
    else:
        print(pilihan, "tidak terdapat dalam menu")
    pertanyaan = input('Apakah Anda ingin menampilkan menu kembali? (y/t) : ')
