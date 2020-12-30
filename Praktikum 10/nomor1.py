try:
    direktori = input('Masukkan direktori file Anda : ')
    buka_file = open(direktori,'r')
    genap=[]
    ganjil=[]
    bilangan=[]

    for list_bilangan in buka_file:
        bilangan.append(int(list_bilangan))

    for list_bilangan in bilangan:
        print(list_bilangan)
        if (list_bilangan % 2 == 0):
            genap.append(int(list_bilangan))
        else:
            ganjil.append(int(list_bilangan))

    print('Banyaknya bilangan genap adalah',len(genap))
    print('Banyaknya bilangan ganjil adalah',len(ganjil))
    
except FileNotFoundError:
    print('Direktori yang Anda masukkan salah')