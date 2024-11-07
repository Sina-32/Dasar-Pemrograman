'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
def fibonacci():
    n = int(input("Masukkan Fibonacci yang diinginkan: "))
    a, b = 0, 1
    
    for i in range(n):
        print(a)
        nilai_sementara = a
        a = b
        b =  nilai_sementara + b

fibonacci()
