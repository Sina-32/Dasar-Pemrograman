'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
jumlah = 0

while True:
    angka = int(input("Masukkan angka (masukkan angka negatif jika ingin berhenti): "))
    if angka < 0:
        break
    jumlah += angka
print("Jumlah:", jumlah)