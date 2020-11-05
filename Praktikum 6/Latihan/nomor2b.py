def starFormation2(n):
    print('*' * n)
    while(n > 0):
        n -= 1
        print('*' * n)


input_bintang = int(input('Masukkan jumlah bintang yang diinginkan : '))
starFormation2(input_bintang)
