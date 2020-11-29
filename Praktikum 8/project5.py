def kuadrat(bil):
    kuadrat = 0
    list_bilangan = []
    for i in range(len(bil)):
        kuadrat = bil[i]**2
        list_bilangan.append(kuadrat)
    return print(list_bilangan)


n = int(input("Masukkan banyak bilangan yang ingin Anda olah : "))
list_kuadrat = []
for i in range(n):
    i += 1
    print(f'Masukan angka ke-{i} : ', end=" ")
    x = int(input())
    list_kuadrat.append(x)
print(list_kuadrat)
print(sum(list_kuadrat))
kuadrat(list_kuadrat)
