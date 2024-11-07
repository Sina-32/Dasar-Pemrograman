'''
Nama : Sina
Nim : 2400606
Kelas : 1B
'''

a = ["Mangga","Alpukat","Jeruk","Strawberry"]
print(len(a)) #menghitung jumlah karakter

a = ["Mangga","Alpukat","Jeruk","Strawberry"]
print(a[3]) #untuk mengambil satu nilai

a = ["Mangga","Alpukat","Jeruk","Strawberry"]
print(a[0:3]) #untuk mengambil nilai 0>3

a = ["Mangga","Alpukat","Jeruk","Strawberry"]
a.append("Buah Naga")
print(a) #untuk menambahkan list di akhir

a = ["Mangga","Alpukat","Jeruk","Strawberry"]
a[1] = "Manggis" #untuk mengubah list dalam nilai 1
print(a)

a = ["Mangga","Alpukat","Jeruk","Strawberry"]
a.insert(1,"Semangka") #untuk menambahkan list di antara item dengan menyisipkan nilainya
print(a)

a = ["Mangga","Alpukat","Jeruk","Starwbery","Alpukat"]
a.remove("Alpukat") #menghapus list dengan menyebutkan value nya
print(a)

a = ["Mangga","Alpukat","Jeruk","Starwbery"]
a.pop(2) #menghapus list dengan menyebutkan indexnya
print(a)

a = ["Mangga","Alpukat","Jeruk", 26,"Starwbery", False, 621.988]
print(a) #penulisan tipe data selain string tidak perlu tanda kutip

a = ["Mangga","Alpukat","Jeruk","Starwbery"]
b = ["Blueberry","Ceri"]
a.extend(b) #berfungsi untuk menggabungkan list a dan list b
print(a) 

a = ["Mangga","Alpukat","Jeruk","Starwbery"]
a.sort() #untuk mengurutkan item dalam list tersebut sesuai abjad
print(a)

a = ("Mangga","Alpukat","Jeruk","Starwbery")
x = list(a) #untuk momodifikasi tuple menjadi tipe data list
x[1] = "Melon" #untuk mengubah list dalam nilai 1
a = tuple(x) #untuk mengembalikan tipe datanya menjadi tuple kembali
print(a)

a = ("Mangga","Alpukat","Jeruk","Starwbery")
x = list(a)
x.insert(3,"Melon") #untuk menambahkan list di antara item dengan menyisipkan nilainya
a = tuple(x)
print(a)

a = ("Mangga","Alpukat","Jeruk","Starwbery")
x = list(a)
x.append("Buah Naga") #untuk menambahkan list di akhir
a = tuple(x)
print(a)

a = ("Mangga","Alpukat","Jeruk","Starwbery")
x = list(a)
x.pop(2)
a = tuple(x) #menghapus list dengan menyebutkan nilainya
print(a)