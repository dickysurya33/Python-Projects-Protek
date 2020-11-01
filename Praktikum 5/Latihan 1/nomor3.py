basindo = int(input("Masukkan nilai Bahasa Indonesia Anda => "))
matik = int(input("Masukkan nilai Matematika Anda       => "))
ipa = int(input("Masukkan nilai Ipa Anda              => "))

print("----------LAMPIRAN KELULUSAN----------\n")
if ((basindo > 100) or (basindo < 0)) or ((ipa > 100) or (ipa < 0)) or ((matik > 100) or (matik < 0)):
    print("Maaf input ada yang tidak valid \n")
elif ((basindo >= 60) and (basindo <= 100) and (matik >= 70) and (matik <= 100) and (ipa >= 60) and (ipa <= 100)):
    status = "Lulus"
    print("Status Kelulusan: ", status, "\n")
else:
    status = "Tidak Lulus"
    print("Status Kelulusan: ", status, "\n")
    print("Sebab => \n")
if basindo > 100 and basindo < 0:
    print(" ")
elif basindo < 60:
    print("Nilai Bahasa Indonesia dibawah 60 \n")
if matik > 100 and matik < 0:
    print(" ")
elif matik < 70:
    print("Nilai Matematika dibawah 70 \n")
if ipa > 100 and ipa < 0:
    print(" ")
elif ipa < 60:
    print("Nilai Ipa dibawah 60 \n")

print("----------TETAP BELAJAR DAN TERUS SEMANGAT----------")
