try:
    input_direktori = input(r'Masukkan direktori dari file Anda : ')
    file = open(input_direktori, 'r')
    print('Berikut ini adalah daftar file pada direktori Anda : ')
    print(file.read())
    file.close()
except (FileNotFoundError):
    print('Direktori yang Anda masukkan salah \nSilahkan periksa direktori file kembali')
except (PermissionError):
    print('Direktori yang Anda masukkan salah \nSilahkan periksa direktori file kembali')
