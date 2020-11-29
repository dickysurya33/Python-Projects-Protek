buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
print("Program penjualan buah")
print("Daftar harga buah per kg")
for i in buah:
    print(f'{i} : {buah[i]}')
total_harga = []
while True:
    input_beli = input("Nama buah yang ingin dibeli : ")
    if input_beli in buah:
        try:
            jumlah_kg = float(input("jumlah kilogram             : "))
            harga1 = jumlah_kg * buah[input_beli]
            total_harga.append(harga1)
            pertanyaan = input("Apakah Anda ingin membeli buah lagi? (y/t) : ")
            if (pertanyaan != 'y'):
                print("-------------------------------")
                print("Total harga                 : Rp", sum(total_harga))
                break
        except (ValueError):
            print("Input yang Anda masukkan tidak valid")

    elif (input_beli == '') or (input_beli not in buah):
        print(input_beli, 'tidak ada dalam daftar')
        break
