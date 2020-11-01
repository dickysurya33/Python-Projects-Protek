count = 0
total = 0
for i in range(1, 100):
    if i % 2 == 0:
        continue
    jumlah = i + 1
    count += 1
    total = total+jumlah
    print(i)

print("Banyaknya bilangan ganjil : ", count)
print("Jumlah seluruh bilangan ganjil adalah", (total - 50))
