print("----------------------+ Program Enkripsi Caesar +----------------------")

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

result = ''

def enkripsi(abjad):
    str = input("String : ") 
    key = int(input("Key : ")) 

    str = str.lower() 
    result = '' 

    for char in str: 
        if char in abjad: 
            n = abjad.index(char) 
            encrypt = (n + key) % 26 
            convert = abjad[encrypt] 
            result = result + convert
        else:
            result = result + ' ' 
    print(f"Result : {result}") 


pilihan = 'y'

while (pilihan == 'y'):
    print("Menu yang tersedia : ")
    print("1. Enkripsi Data")
    print("2. Keluar")

    menu = input("Menu yang dipilih : ")
    print("-------------------------------------")

    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(abjad)
    elif menu == '2':
        print("Program Selesai, terima kasih.")
        break
    else:
        print("Menu tidak ditemukan")


    print("------------------------------------")
    pilihan = input("Apakah ingin melanjutkan ? (Y/n) : ")
    print("------------------------------------")