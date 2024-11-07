'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
bebek = int(input("Masukan Jumlah Bebek Kecil : "))
while bebek > 0:
    print(f"{bebek} bebek kecil berenang")
    print(f"Menyusuri sungai yang deras")
    print(f"Induknya mencari kwek kwek kwek")
    bebek -= 1
    if bebek > 0:
        print(f"Hanya {bebek} ekor yang pulang")
    else:
        print(f"Dan semua bebek kecil pulang, aha!")