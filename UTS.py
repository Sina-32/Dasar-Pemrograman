print("Silahkan Login")

def login():
    username_terdaftar = "Daspro2024"
    password_terdaftar = "Latihan"
    kesempatan = 5

    while kesempatan > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == username_terdaftar and password == password_terdaftar:
            print("Login berhasil!")
            return

        elif username == username_terdaftar:
            print(f"Password salah. Kesempatan tersisa: {kesempatan-1}")
        elif password == password_terdaftar:
            print(f"Username salah. Kesempatan tersisa: {kesempatan-1}")
        else:
            print(f"Username dan password salah. Kesempatan tersisa: {kesempatan-1}")

        kesempatan -= 1

    print("Anda telah keluar dari sistem login")

login()
