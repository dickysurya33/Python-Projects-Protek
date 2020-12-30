nomor2 = open('nomor2.txt', 'r')
no2 = nomor2.readlines()
dictionary = []

for dicti in range (len(no2)):
    data_no2 = no2[dicti]
    data_no3 = data_no2.split("|")
    list_dictionary = {"nim" : data_no3[0],"nama" : data_no3[1], "alamat" : data_no3[2]}
    dictionary.append(list_dictionary)

print("dataMhs = ", dictionary)
nomor2.close()