from random import randint
tebakan_komputer = randint(0, 100)

print("Halo... Nama saya Super Computer ")
print("Saya telah memilih bilangan secara acak dari 0 - 100")
print("Coba tebak, bilangan berapakah itu?? ")

while True:
    angka_user = int(input("Silakan masukkan tebakan Anda : "))

    if (angka_user > 0) and (angka_user < tebakan_komputer):
        print("Yah maaf gan, bilangan Anda terlalu kecil")
    elif (angka_user < 100) and (angka_user > tebakan_komputer):
        print("Ups masih kurang tepat, bilangan Anda terlalu besar")
    elif (angka_user == tebakan_komputer):
        print("Wadidaw mantap tebakan Anda tepat :>")
        break
    else:
        print("Ingat bro, angkanya cuma 0 - 100 ")
        continue
