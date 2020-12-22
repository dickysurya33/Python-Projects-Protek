try:
    input_bintang=int(input('Masukkan jumlah baris : '))
    def bintang(n):
        baris_atas = 0
        bintang_atas = 1
        while baris_atas < n/2 :
            output = '*' * bintang_atas
            print (output.center(2*n))
            bintang_atas+= 2
            baris_atas+= 1

        bintang_bawah = n - 2
        baris_bawah = (n - baris_atas) + 1

        while (baris_bawah >= n/2):
            output = '*' * bintang_bawah
            bintang_bawah -= 2
            baris_bawah += 1
            print(output.center(2*n))
            if baris_bawah == n:
                break

    bintang (input_bintang)
except ValueError:
    print('Input yang Anda masukkan salah')