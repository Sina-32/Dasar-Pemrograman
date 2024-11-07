a = {"apel", "jeruk", "ceri", "blueberry"}
print(a) #set menampilkan data dengan urutan random

a = {"apel", "jeruk", "ceri", "blueberry"}
a.add("semangka")
print(a) #menambahkan data dengan penempatan random

a = {"apel", "jeruk", "ceri", "blueberry"}
b = {"strawbery", "nanas"}
a.update(b) #menggabungkan data dengan penempatan random
print(a)

a = {"apel", "jeruk", "ceri", "blueberry"}
b = {"strawbery", "nanas", "apel", "jeruk"}
a.intersection_update(b) #menambahkan dua buah set yang berbeda tanpa variabel baru
print(a)

a = {"apel", "jeruk", "ceri", "blueberry"}
b = {"strawbery", "nanas", "apel", "jeruk"}
a.intersection(b) #menambahkna dua buah set yang sama
print(a)

a = {1, 2, 3, 4}
b = {1,3, 5, 7}
a.symmetric_difference(b)
print(a)

a = {1, 2, 3, 4}
b = {1,3, 5, 7}
a.symmetric_difference_update(b)
print(a)

a = {"apel", "jeruk", "ceri", "blueberry"}
b = {"strawbery", "nanas", "apel", "jeruk"}
a.update(b)
print(a)

a = {"apel", "jeruk", "ceri", "blueberry"}
a.remove("ceri") #menghapus item menggunakan variabel nya
print(a)

a = {"apel", "jeruk", "ceri", "blueberry"}
a.pop() #menhapus item secra random
print(a)

a = {"apel", "jeruk", "ceri", "blueberry"}
a.clear() #menghapus semua item dalam set
print(a)

kucing = {
    "nama":"oren",
    "nama":"garfil",
    "umur":"3 tahun",
    "ras":"american shorthair",
    "jantan":True,
    "hobi":["makan","tidur"]
}
print(len(kucing)) #mengecek jumlah item dalam dictionery

buah = dict(nama = 'apel', warna='merah', manis=True)
print(buah)

kucing = {
    "nama":"oren",
    "nama":"garfil",
    "umur":"3 tahun",
    "ras":"american shorthair",
    "jantan":True,
    "hobi":["makan","tidur"]
}
print(kucing.keys())

kucing = {
    "nama":"oren",
    "nama":"garfil",
    "umur":"3 tahun",
    "ras":"american shorthair",
    "jantan":True,
    "hobi":["makan","tidur"]
}
print(kucing.values())

kucing = {
    "nama":"oren",
    "nama":"garfil",
    "umur":"3 tahun",
    "ras":"american shorthair",
    "jantan":True,
    "hobi":["makan","tidur"]
}
print(kucing)
kucing["umur"]=3

kucing = {
    "nama":"oren",
    "nama":"garfil",
    "umur":"3 tahun",
    "ras":"american shorthair",
    "jantan":True,
    "hobi":["makan","tidur"]
}
kucing.update({'umur':3,'ras':'brithis'})
print(kucing)

kucing = {
    "nama":"oren",
    "nama":"garfil",
    "umur":"3 tahun",
    "ras":"american shorthair",
    "jantan":True,
    "hobi":["makan","tidur"]
}
kucing.update({"warna":["oren","belang-belang"]})
print(kucing)

kucing = {
    "nama":"oren",
    "nama":"garfil",
    "umur":"3 tahun",
    "ras":"american shorthair",
    "jantan":True,
    "hobi":["makan","tidur"]
}
kucing.pop("jantan")
print(kucing) #menghapus dengan menyebutkan variabelnya

