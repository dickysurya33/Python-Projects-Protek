kata=str(input('Masukkan kata yang ingin Anda masukkan : '))
kata_lower=kata.lower()
huruf_ubah=str(input('Masukkan huruf yang ingin Anda ubah : '))
huruf_ubah_lower=huruf_ubah.lower()
perubahan=str(input('Masukkan huruf pengganti : '))
perubahan_lower=perubahan.lower()

def ubah(teks, a, b):
    list_teks = list(teks)
    output = '' 
    
    for huruf in list_teks:
        if huruf == a:
            huruf = b
        output = ''.join([output,huruf])
    return output
    
print(ubah(kata_lower,huruf_ubah_lower,perubahan_lower))