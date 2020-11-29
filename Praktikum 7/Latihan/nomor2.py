try:
    input_direktori = input(r"Silahkan masukkan direktori file Anda : ")
    file = open(input_direktori, "r")
    kondisi = True
    # untuk menambahkan data a=append
    file = open(input_direktori, "a")
    # pertanyaan untuk menambah file atau tidak
    while (kondisi == True):
        tambah_file = input(str('Masukkan file yang ingin Anda tambahkan '))
        file.write(tambah_file)
        file.write('\n')
        pertanyaan = input(
            'Apakah Anda ingin menambahkan file kembali? (y/t) : ')
        if (pertanyaan == 't'):
            kondisi = False
            file = open(input_direktori, 'r')
            print('Berikut adalah file yang terdapat pada direktori Anda')
            print(file.read())
            file.close()
except (FileNotFoundError):
    print('Direktori yang Anda masukkan salah \nSilahkan periksa direktori file kembali')
except (PermissionError):
    print('Direktori yang Anda masukkan salah \nSilahkan periksa direktori file kembali')
