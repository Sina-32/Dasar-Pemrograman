'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
Input_NIM=int(input("Input 3 digit NIM terakhir : "))
if range (1, 51):
    menentukan_bilangan = Input_NIM % 2
    if menentukan_bilangan == 0:
        print("Silakan masuk ke kelas K1")
    else:
        print("Silakan masuk ke kelas K2")
elif range (51, 101):
    menentukan_bilangan = Input_NIM % 2
    if menentukan_bilangan == 0:
        print("Silakan masuk ke kelas K3")
    else:
        print("Silakan masuk ke kelas K4")
elif range (101, 150):
    menentukan_bilangan = Input_NIM % 2
    if menentukan_bilangan == 0:
        print("Silakan masuk ke kelas K5")
    else:
        print("Silakan masuk ke kelas K6")
elif Input_NIM>151:
    menentukan_bilangan = Input_NIM % 2
    if menentukan_bilangan == 0:
        print("Silakan masuk ke kelas K7")
    else:
        print("Silakan masuk ke kelas K8")  



