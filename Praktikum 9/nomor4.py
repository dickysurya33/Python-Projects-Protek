try:
    import random

    kata = str(input('Masukkan kata : '))
    kombinasi=int(input('Masukkan banyaknya kombinasi : '))

    def shuffleString (x, n):
        list_kata = []
        while (len(list_kata) < n):
            random_kata = random.sample(x, len(x))
            kombinasi = ''.join(random_kata)
            if kombinasi not in list_kata :
                list_kata.append(kombinasi)

        print (list_kata)


    shuffleString(kata, kombinasi)
except ValueError:
    print('Input yang Anda masukkan salah')