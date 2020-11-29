def sortStringByChar(karakter):
    karakter.sort(reverse=True, key=len)
    return print(karakter)


list_buah = []
n = int(input('Masukkan banyak buah yang Anda inginkan : '))
for i in range(n):
    i += 1
    print(f'Buah ke-{i} : ', end='')
    x = input('')
    list_buah.append(x)

print(list_buah)
# urut berdasar karakter terpanjang
print('urut berdasar karakter terpanjang')
sortStringByChar(list_buah)
