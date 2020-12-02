def nilai(x):
    namaMhs = {}
    nimMhs = {}
    for i in range(len(x)):
        nilai_akhir = ((x[i]['mid']) + (2*(x[i]['uas'])))/3
        namaMhs[x[i]['nama']] = nilai_akhir
        nimMhs[x[i]['nim']] = nilai_akhir
    namaMax = max(namaMhs, key=namaMhs.get)
    nimMax = max(nimMhs, key=nimMhs.get)
    print("Mahasiswa dengan nilai tertinggi adalah",
          namaMax, "( NIM : ", nimMax, ")")


nilaiMhs = [{'nim': 'A01', 'nama': 'Amir', 'mid': 50, 'uas': 80},
            {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
            {'nim': 'A03', 'nama': 'Cici', 'mid': 50, 'uas': 50},
            {'nim': 'A04', 'nama': 'Dedi', 'mid': 20, 'uas': 30},
            {'nim': 'A05', 'nama': 'Fifi', 'mid': 70, 'uas': 40}]


nilai(nilaiMhs)
