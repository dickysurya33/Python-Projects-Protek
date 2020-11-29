def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    output = [a, b, c]
    return print(output)


try:
    n = int(input("Masukkan jumlah bilangan yang ingin Anda olah : "))
    list_bilangan = []
    for i in range(n):
        i += 1
        print(f'Masukan angka ke-{i} : ', end=" ")
        x = int(input())
        list_bilangan.append(x)
    tuple_bilangan = tuple(list_bilangan)
    dataStat(tuple_bilangan)
except(ValueError):
    print('Input yang Anda masukkan salah')
except(NameError):
    print('Input yang Anda masukkan salah')
