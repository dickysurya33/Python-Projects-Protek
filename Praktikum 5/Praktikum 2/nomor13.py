from random import randint
sum = 0
while True:
    bil = randint(0, 10)
    print(bil)
    sum += 1
    if (bil == 5):
        print("Jumlah perulangan : ", sum)
        break
