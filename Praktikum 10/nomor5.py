file  = open ('nomor5.txt', 'r')
hasil = input('Masukkan nama file dalam (.txt)  : ')
output= open(hasil, 'w+')
for hasil_jumlah in file:
    pemecahan = hasil_jumlah.split('|')
    hasil = int(pemecahan[0]) + int(pemecahan[1])
    output.write(str(hasil))
    output.write('\n')
    
output.close()