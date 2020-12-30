file = open('nomor2.txt', 'r')
list_file = file.readlines()
list_dictionary = []
nim  = input('Masukkan NIM yang mau dicari: ')
for split in list_file:
    pecah = split.split('|')
    dictionary = {'nim': pecah[0],'nama': pecah[1],'alamat': pecah[2]}
    list_dictionary.append(dictionary)

if nim == list_dictionary[0]['nim'] :
    print('Data Mahasiswa')
    print('NIM      : ',list_dictionary[0]['nim'])
    print('Nama     : ',list_dictionary[0]['nama'])
    print('Alamat   : ',list_dictionary[0]['alamat'])
else:
    print('"Data mahasiswa tidak ditemukan"')
