a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

# menambahkan 10 dan 15 ke indeks ke-3 dan ke-2
a.insert(3, 10)
b.insert(2, 15)

# menambahkan 4 dan 8 di indeks terakhir
a.append(4)
b.append(8)

# mengurutkan list a dan b dengan sort ascending
a.sort()
b.sort()

# membuat list c dengan mengambil data dari list a indeks ke-0 sampai 7
c = a[:8]
# membuat list d dengan mengambil data dari list b indeks ke-2 sampai 9
d = b[2:10]

# membuat list e dengan syarat e[c0+d0,c1+d1,.....]
e = []
for i in range(len(d)):
    e += [c[i] + d[i]]
# mengubah list e ke dalam tuple
e = tuple(e)

# mencari nilai minimal
minimal = min(e)
# mencari nilai maksimal
maksimal = max(e)
# mencari hasil penjumlahan dari semua elemen e
hasil = sum(e)

print('nilai minimal dari  e adalah : ', minimal)
print('nilai maksimal dari  e adalah : ', maksimal)
print('nilai penjumlahan seluruh elemen e adalah : ', hasil)

# membuat list myString
myString = "python adalah bahasa pemrograman yang menyenangkan"
# mengubah list myString ke dalam bentuk set
setMyString = set(myString)

# mengubah nilai setMyString ke dalam list
listSetMyString = list(setMyString)
print('\nlist myString\n', listSetMyString)
# mengurutkan dengan sort ascending listSetMyString
listSetMyString.sort()
print('\nlist myString diurutkan dengan sort ascending\n', listSetMyString)
