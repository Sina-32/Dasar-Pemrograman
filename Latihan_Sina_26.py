'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
jam_mulai = int(input("Masukkan jam mulai: "))
menit_mulai = int(input("Masukkan menit mulai: "))
detik_mulai = int(input("Masukkan detik mulai: "))

jam_selesai = int(input("Masukkan jam selesai: "))
menit_selesai = int(input("Masukkan menit selesai: "))
detik_selesai = int(input("Masukkan detik selesai: "))

def selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):

    mulai_detik = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    selesai_detik = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
    selisih_detik = selesai_detik - mulai_detik

    jam = selisih_detik // 3600
    menit = (selisih_detik % 3600) // 60
    detik = selisih_detik % 60

    print( f"{jam} jam - {menit} menit - {detik} detik")

selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)
