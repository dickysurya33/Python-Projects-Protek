try:
    file = open("d:/data.txt", "r")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except (ValueError):
    print('Mohon maaf terjadi kesalahan dalam file data.txt,Silahkan periksa kembali file Anda')
# Program by Dicky Surya Nanda
