tar_mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gilang", "Hani", "Indra", "Joko", "Kiki", "Lia", "Mira", "Nina", "Oki", "Putu", "Rani", "Santi", "Tomi", "Umi"]

cari_nama = input("Masukkan nama mahasiswa yang ingin dicari: ")

def linear_search_nama(daftar_mahasiswa, cari_nama):
    for item in cari_nama:
        if item.lower() == daftar_mahasiswa.lower():
            return True
    return False

if linear_search_nama(cari_nama, daftar_mahasiswa):
    print(f"{cari_nama} tersedia dalam data.")
else:
    print(f"{cari_nama} tidak tersedia dalam data.")