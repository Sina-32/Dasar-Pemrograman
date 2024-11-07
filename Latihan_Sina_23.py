'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
def oprasi(angka):
    total = sum(angka)
    rata_rata = total / len(angka)
    print(f"Input: {angka}")  
    print(f"Total: {total}")
    print(f"Rata-rata: {rata_rata}")

angka = []  
while True:
    angka_input = int(input("Masukkan angka (masukkan angka 0 jika ingin berhenti): "))
    if angka_input == 0:  
        break
    angka.append(angka_input)
    
oprasi(angka)



