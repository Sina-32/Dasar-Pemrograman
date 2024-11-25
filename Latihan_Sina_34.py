'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
stok_barang = ["Beras", "Gula", "Minyak", "Teh", "Kopi", "Susu", "Mie", "Telur", "Kecap", "Garam", "Sabun", "Shampoo", "Lilin", "Tissue", "Mentega"]

cari_barang = input("Masukkan nama barang yang ingin dicari: ")

def linear_search_barang(stok_barang, cari_barang):
    for item in cari_barang:
        if item.lower() == stok_barang.lower():
            return True
    return False

if linear_search_barang(cari_barang, stok_barang):
    print(f"{cari_barang} tersedia dalam stok.")
else:
    print(f"{cari_barang} tidak tersedia dalam stok.")