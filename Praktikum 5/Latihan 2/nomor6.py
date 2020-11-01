from random import randint
tebakan_komputer = randint(0, 100)
nilai = 0

print("Halo... Nama saya Super Computer ")
print("Saya telah memilih bilangan secara acak dari 0 - 100")
print("Coba tebak, bilangan berapakah itu?? ")

while True:
    angka_user = int(input("Silakan masukkan tebakan Anda : "))

    if (angka_user > 0) and (angka_user < tebakan_komputer):
        print("Yah maaf gan, bilangan Anda terlalu kecil")
        nilai += 1
    elif (angka_user < 100) and (angka_user > tebakan_komputer):
        print("Ups masih kurang tepat, bilangan Anda terlalu besar")
        nilai += 1
    elif (angka_user == tebakan_komputer):
        print("Wadidaw mantap tebakan Anda tepat :>")
        skor = 100 - (nilai * 2)
        if (skor > 0):
            print("Skor Anda adalah: ", skor)
        else:
            print("Waduuh gawat....Nilai kamu 0, Eitss tenang bisa diulangi kok :v")
        break
    else:
        print("Ingat bro, angkanya cuma 0 - 100 ")
        continue
