'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''

def login():
    password_terdaftar = "Latihan"
    kesempatan = 3
    
    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if password == password_terdaftar:
            print("Login berhasil!")
            return
        else:
            kesempatan -= 1
            print(f"Password salah! Kesempatan tersisa: {kesempatan}")
    
    print("Anda telah keluar dari sistem login.")

login()
