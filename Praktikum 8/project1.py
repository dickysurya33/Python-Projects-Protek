try:
    n = int(input("Masukkan banyaknya bilangan yang ingin Anda masukkan : "))
    i = 0
    list_bilangan = []
    while (i < n):
        i += 1
        print(f'Bilangan ke-{i} : ', end='')
        bilangan = int(input(''))
        list_bilangan.append(bilangan)

    list_bilangan.sort(reverse=True)
    print('list dengan sort descending : ', list_bilangan)
except (ValueError):
    print('Bilangan yang Anda masukkan tidak valid/salah')
