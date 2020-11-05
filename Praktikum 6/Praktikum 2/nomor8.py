def luasSegitiga(a, t):
    luas = a * t / 2
    return luas


# segitiga 1
alas = 10
tinggi = 20
print('Luas segitiga dengan alas', alas, ' dan tinggi',
      tinggi, ' adalah', luasSegitiga(alas, tinggi))
# segitiga 2
alas1 = 15
tinggi1 = 45
print('Luas segitiga dengan alas', alas1, ' dan tinggi',
      tinggi1, ' adalah', luasSegitiga(alas1, tinggi1))
# luas total
a = luasSegitiga(alas, tinggi) + luasSegitiga(alas1, tinggi1)
print('Luas total dari kedua segitiga tersebut adalah', a)
