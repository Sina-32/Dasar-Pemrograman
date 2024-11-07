'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
suami = ["Suami 1", "Suami 2", "Suami 3"]
istri = ["Istri 1", "Istri 2", "Istri 3"]

for i in range(2):
    print(f"{suami[i]} dan {istri[i]} ke seberang sungai")
    print(f"{suami[i]} kembali ke dermaga")
    if i == 0:
        print(f"Di Dermaga Ada {istri[1]} {istri[2]} {suami[0]} {suami[1]} {suami[2]} Dan Di Seberang Sungai Ada {istri[0]}")
    elif i == 1:
        print(f"Di Dermaga Ada {istri[2]} {suami[0]} {suami[1]} {suami[2]} Dan Di Seberang Sungai {istri[0]} {istri[1]}")

print(f"{suami[2]} dan {istri[2]} ke seberang sungai")
print(f"Di Dermaga Ada {suami[0]} {suami[1]} Dan Di Seberang Sungai {istri[0]} {istri[1]} {istri[2]} {suami[2]}")

for i in range(2):
    print(f"{istri[i]} kembali ke dermaga")
    print(f"{suami[i]} dan {istri[i]} ke seberang sungai")
    if i == 0:
        print(f"Di Dermaga Ada {suami[1]} Dan Di Seberang Sungai {istri[0]} {istri[1]} {istri[2]} {suami[0]} {suami[2]}")
    elif i == 1:
        print(f"Sekarang Di Seberang Sungai Ada {istri[0]} {istri[1]} {istri[2]} {suami[0]} {suami[1]} {suami[2]}")

print("Semua orang sudah menyeberang")
