'''
Nama : Sina
Nim : 2400606
Kelas : 1B
'''
student_info={
    "Alice": {"Age":20, "Major":"Computer Science"},
    "Bob": {"Age":21, "Major":"Mathematics"},
    "Charlie": {"Age":19, "Major":"Physics"}
}
nama=input("Nama: ")
info = student_info.get(nama)
umur = info.get("Age") # Ambil umur
jurusan = info.get("Major") # Ambil jurusan
print(f"Umur {nama} adalah {umur} dan prodinya adalah {jurusan}")