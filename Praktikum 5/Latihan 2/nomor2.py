sum = 0
for i in range(1, 100):
    if i % 2 == 0:
        continue
    sum += 1
    print(i)

print("Banyaknya bilangan ganjil : ", sum)
