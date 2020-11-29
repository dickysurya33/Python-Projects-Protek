n = int(input("Masukkan banyaknya nama yang ingin Anda masukkan : "))
i = 0
nama = []
while (i < n):
    i += 1
    print(f'Nama ke-{i} : ', end='')
    input_nama = str(input(''))
    nama.append(input_nama)
nama.sort()
print('Nama setelah diurutkan dengan sort ascending :', nama)
for karakter in nama:
    print(f'Panjang karakter dari {karakter} adalah', len(
        karakter), 'karakter')
