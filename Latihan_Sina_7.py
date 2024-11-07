'''
Nama : Sina
Nim : 2400606
Kelas : 1B
'''
nilai_mahasiswa = [88,75,63,97,82,74,91,80,81,63]
nilai_max = max(nilai_mahasiswa)
nilai_min = min(nilai_mahasiswa)
rata_rata = sum(nilai_mahasiswa)/len(nilai_mahasiswa)
print(f"Nilai Terbesar adalah {nilai_max}")
print(f"Nilai Terkecil adalah {nilai_min}")
print(f"Rata-Rata Nilai Mahasiswa adalah {rata_rata}")
nilai_mahasiswa.sort(reverse=True)
print(nilai_mahasiswa)
print(f"Nilai terbesar ke-2 adalah {nilai_mahasiswa[1]}")