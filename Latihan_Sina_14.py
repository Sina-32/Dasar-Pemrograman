'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
Bilangan=int(input("Bilangan : "))
if(Bilangan == 0):
    print(f"{Bilangan} adalah {Bilangan}")
elif(Bilangan%2==0):
    if(Bilangan<0):
        print(f"{Bilangan} adalah bilangan negatif dan termasuk bilangan genap")
    elif(Bilangan>0):
        print(f"{Bilangan} adalah bilangan positif dan termasuk bilangan genap")
else:
    if(Bilangan<0):
        print(f"{Bilangan} adalah bilangan negatif dan termasuk bilangan ganjil")
    elif(Bilangan>0):
        print(f"{Bilangan} adalah bilangan positif dan termasuk bilangan ganjil")
