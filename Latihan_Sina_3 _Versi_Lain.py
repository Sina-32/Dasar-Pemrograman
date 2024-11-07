from datetime import datetime
'''
Nama : Sina
Nim : 2400606
Kelas : 1B
'''
nama = input("Nama : ")
tahun_lahir = int(input("Tahun Lahir : "))
tahun_ini = datetime.now().year
umur = tahun_ini - tahun_lahir
print(f"Selamat Datang {nama} umur kamu {umur}")