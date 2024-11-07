'''
Nama : Sina
Nim : 2400606
Kelas : 1B
'''
# Nomor 1
List = ["apel","jeruk","ceri","duria","apel","mangga"]
List[2] = "cherry"
print(List)

# Nomor 2
List = ["apel","jeruk","ceri","duria","apel","mangga"]
Nomor = input("Nomor : ")
Nama = input("Nama : ")
List.insert( int(Nomor), str(Nama))
print(List)

# Nomor 3
List.sort()
print(List)
