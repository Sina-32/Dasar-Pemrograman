'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
import numpy as np

nilai_ujian = np.array([85, 92, 78, 88, 76, 95, 89, 82, 67, 91, 74, 81, 93, 77, 84, 90, 69, 65, 100, 79, 85, 66, 80, 87, 92, 94, 98, 72, 73, 81])

nilai_ujian_urut = np.sort(nilai_ujian)
print(f"Nilai ujian siswa: {nilai_ujian_urut}")

nilai_terbesar = nilai_ujian_urut[-5:]
print(f"Nilai terbesar: {nilai_terbesar}")