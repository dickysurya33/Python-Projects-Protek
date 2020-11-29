def rata2(buah):
    harga = list(buah.values())
    rata_rata = sum(buah.values())/len(harga)
    return print('Rata-rata harga adalah', rata_rata)


daftar_buah = {"apel": 5000,
               "jeruk": 8500,
               "mangga": 7800,
               "duku": 6500}
rata2(daftar_buah)
