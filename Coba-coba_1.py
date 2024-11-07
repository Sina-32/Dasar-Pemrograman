jumlah_perulangan=5
for index in range(jumlah_perulangan):
    print(index) #menampilkan angka dari 0

for i in range(6):
    print(i) #menampilkan angka dari 0

for i in range(1, 6):
    print(i) #menampilkan angka 1-5/ jika ingin memulai suatu perulangan dari angka tertentu

for i in range(2, 6):
    print(i) #menampilkan angka 2-5/ jika ingin memulai suatu perulangan dari angka tertentu

for i in range(1, 10, 2):
    print(i) #menampilkan angka dari 1-10 yang kelipatan 2

for i in "Sina":
    print(i)

buah=['apel','anggur','strawberry','blueberry']
for i in buah:
    print(f"Buah : {i}") #melakukan perulangan sampai data selesai

angka=0
while(angka<=10): #angka kurang sama dengan 10
    print(f"Angka : {angka}")
    angka+=1 #untuk menambah 1

angka=[1,2,3,4,5]
for i in angka:
    print(i) #angka berhenti sampai 3
    if i == 3:
        break 

angka=[1,2,3,4,5]
for i in angka:
    if i == 3:
        break 
    print(i) #angka berhenti sampai 2

angka=[1,2,3,4,5]
for i in angka:
    if i == 3:
        continue 
    print(i) #angka akan melewati angka 3

jumlah = 0
angka=0
while angka >= 0: #jika angka negatif akan berhenti
    angka = int(input("Masukkan angka (masukkan angka negatif jika ingin berhenti): "))
    if angka < 0: #tidak menghitung angak negatif
        break
    jumlah += angka
print("Jumlah:", jumlah)

buah=['apel','anggur','strawberry','blueberry']
angka=[1,2,3]
for i in buah:
    for j in angka:
        print(i)
        print(j)

kata="kata"
for karakter in kata:
    if karakter == "k":
        continue
    print(f"Huruf {karakter}")

baris=0
bintang=0
while baris < 10:
    if(bintang>=baris+1):
        print()
        baris+=1
        bintang=0
        continue
    print("*", end="")
    bintang += 1