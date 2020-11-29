buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
print("Progam penjualan buah\n")
print("Daftar harga buah per kg")
for i in buah:
    print(f'{i} : {buah[i]}')
while True:
    input_beli = input("Masukkan nama buah yang ingin Anda beli : ")
    if input_beli in buah:
        try:
            jumlah_kg = float(input("jumlah kilogram             : "))
            harga = jumlah_kg * buah[input_beli]
            print("-------------------------------")
            print("Total harga                 : Rp", harga)
            break
        except (ValueError):
            print("Masukkan input yang valid")
            break
    elif (input_beli == '') or (input_beli not in buah):
        print(input_beli, 'tidak ada dalam daftar')
        break
