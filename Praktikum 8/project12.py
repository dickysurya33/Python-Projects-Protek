buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
pertanyaan = 'y'
print("Daftar harga buah per kg\n")
for i in buah:
    print(f'{i} : {buah[i]} per kg')
print('\n')
while (pertanyaan == 'y'):
    print("Menu : ")
    print('A. Beli buah')
    print('B. Tambah daftar buah')
    print('C. Hapus daftar buah')
    print('D. Keluar program')
    menu = input("\nSilakan pilih menu : ")
    total_harga = []
    if (menu.lower() == 'a'):
        while True:
            input_beli = input("Nama buah yang ingin dibeli : ")
            if input_beli in buah:
                try:
                    berat = float(input("Berapa kg             : "))
                    harga1 = berat * buah[input_beli]
                    total_harga.append(harga1)
                    pertanyaan = input(
                        "\nApakah Anda ingin membeli buah lagi? (y/n) : ")
                    if (pertanyaan != 'y'):
                        print("-------------------------------")
                        print("Total harga                 : Rp",
                              sum(total_harga), "\n")
                        break
                except (ValueError):
                    print("Masukkan jumlah yang valid")

            elif (input_beli == '') or (input_beli not in buah):
                print("Buah yang Anda input tidak ada dalam daftar")

    elif (menu.lower() == 'b'):
        kondisi = True
        while (kondisi == True):
            input_buah = input("Masukkan nama buah yang baru : ")
            if input_buah in buah:
                print(input_buah, "sudah terdaftar")
            elif input_buah not in buah:
                try:
                    harga_baru = float(input("Harga per kilogram : "))
                    buah[input_buah] = harga_baru
                    print(input_buah, "berhasil ditambahkan\n")
                    print("Daftar harga baru \n")
                    for data in buah:
                        print(data, buah.get(data), 'per kg')
                        kondisi = False
                    print()
                except (ValueError):
                    print("Masukkan harga yang valid")
    elif (menu.lower() == 'c'):
        kondisi = True
        while (kondisi == True):
            hapus_buah = input("Masukkan buah yang akan dihapus : ")
            if (hapus_buah not in buah):
                print(hapus_buah, "tidak ada dalam daftar")
            elif (hapus_buah in buah):
                del buah[hapus_buah]
                print(hapus_buah, "telah dihapus dari daftar\n")
                print("Daftar buah beserta harga : \n")
                for data in buah:
                    print(data, buah.get(data), 'per kg')
                kondisi = False
    elif (menu.lower() == 'd'):
        print("\nTerimakasih atas kunjungan Anda ke toko kami")
        break
