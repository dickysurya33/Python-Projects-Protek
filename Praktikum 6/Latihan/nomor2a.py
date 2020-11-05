def starFormation1(n):
    bintang = 0
    while(bintang < n):
        bintang += 1
        print('*' * bintang)


input_bintang = int(input("Masukkan jumlah bintang yang diinginkan : "))
starFormation1(input_bintang)
