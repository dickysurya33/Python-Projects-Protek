basindo = int(input("Masukkan nilai Bahasa Indonesia Anda => "))
matik = int(input("Masukkan nilai Matematika Anda       => "))
ipa = int(input("Masukkan nilai Ipa Anda              => \n"))

print("----------LAMPIRAN KELULUSAN----------\n")
if ((basindo >= 60) and (basindo <= 100) and (matik >= 70) and (matik <= 100) and (ipa >= 60) and (ipa <= 100)):
    status = "Lulus"
    print("Status Kelulusan: ", status)
else:
    status = "Tidak Lulus"
    print("Status Kelulusan: ", status, "\n")
print("----------TETAP BELAJAR DAN TERUS SEMANGAT----------")
