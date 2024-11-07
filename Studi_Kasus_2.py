'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
bilangan_genap=0
bilangan_ganjil=0
Input_bilangan=0
while Input_bilangan >=0:
    Input_bilangan=int(input("Input Bilangan : "))
    if Input_bilangan < 0:
        break
    menentukan_bilangan = Input_bilangan % 2
    if menentukan_bilangan == 0:
        bilangan_genap += Input_bilangan
    else: 
        bilangan_ganjil += Input_bilangan 
print(f"Jumlah bilangan genap : {bilangan_genap} ")
print(f"Jumlah bilangan ganjil : {bilangan_ganjil}")



