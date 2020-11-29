def harga_mahal(buah):
    harga = list(buah.values())
    harga_tinggi = max(harga)
    return print('Harga tertinggi adalah :', harga_tinggi)


daftar_buah = {"apel": 5000,
               "jeruk": 8500,
               "mangga": 7800,
               "duku": 6500}
harga_mahal(daftar_buah)
