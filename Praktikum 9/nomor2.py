try:
    input_bintang=int(input('Masukkan jumlah baris : '))
    def bintang(n):
        baris = 0
        bintang = 1
        while baris < n :
            output = '*' * bintang
            print (output.center(2*n))
            bintang+=2
            baris+=1

    bintang (input_bintang)
except ValueError:
    print('Input yang Anda masukkan salah')