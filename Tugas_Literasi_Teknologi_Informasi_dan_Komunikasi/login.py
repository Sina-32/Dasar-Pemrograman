print(f"Silahkan Login")
Login = 3
while Login > 0:
    Username = input("Username : ")
    Password = input("Password : ")

    if Username == "loginUTS" and Password == "rpl2024":
        print("Selamat datang di aplikasi prodi RPL")
        break
    else:
        Login -= 1
        if Login > 0:
            print(f"Login Salah! Kesempatan Anda {Login}x kali lagi")
def login():
    username_terdaftar = "Daspro2024"
    password_terdaftar = "Latihan"
    kesempatan = 3
    
    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username == username_terdaftar and password == password_terdaftar:
            print("Login berhasil!")
            return
        else:
            print(f"Anda tidak diperkenankan mengakses aplikasi ini.")
            kesempatan -= 1
            print(f"Username atau password salah! Kesempatan tersisa: {kesempatan}")
    
    print("Anda telah keluar dari halaman login")
login()