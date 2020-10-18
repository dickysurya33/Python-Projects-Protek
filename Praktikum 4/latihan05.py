# input jumlah
mahasiswa_laki = int(input("jumlah mahasiswa laki laki ="))
mahasiswa_perempuan = int(input("jumlah mahasiswa perempuan ="))

diagram_laki = int(mahasiswa_laki//10)
diagram_perempuan = int(mahasiswa_perempuan//10)

# diagram
print("Diagram batang horizontal Mahasiswa PTIK dalam satu bintangnya(*) mewakili 10 orang =")
print("Mahasiswa Laki-laki =", diagram_laki*"*")
print("Mahasiswa Perempuan =", diagram_perempuan*"*")
