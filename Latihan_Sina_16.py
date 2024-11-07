'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
Jenis_kelamin=input("Jenis Kelamin (P/L) : ")
Umur=int(input("Umur : "))
Tinggi_Badan=int(input("Tinggi Badan : "))
IQ=int(input("IQ : "))

if Jenis_kelamin == "P" and Umur >= 18 and Umur <= 25 and Tinggi_Badan >=170 and IQ >= 130 :
    print(f"Kamu dapat menjadi model catwalk")
elif Jenis_kelamin == "L" and Umur >= 18 and Umur <= 25 and Tinggi_Badan >=175 and IQ >= 130 :
    print(f"Kamu dapat menjadi model catwalk")
else:
  print(f"Kamu tidak bisa menjadi model catwalk")