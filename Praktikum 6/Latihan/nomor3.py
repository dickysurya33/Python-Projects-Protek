from math import factorial


def kombinasi(a, b):
    hasil = factorial(a)/(factorial(a-b)*factorial(b))
    print('Kombinasi', b, 'dari', a, 'adalah :', hasil)


def permutasi(a, b):
    hasil_hitung = factorial(a)/(factorial(a-b))
    print('Permutasi', b, 'dari', a, 'adalah :', hasil_hitung)


kombinasi(5, 3)
permutasi(10, 7)
