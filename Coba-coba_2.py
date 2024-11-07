import random
import tkinter as tk
from tkinter import messagebox

info_acak = [
    "Tahukah kamu? Indonesia memiliki lebih dari 17.000 pulau.",
    "Fakta: Jantung manusia berdetak sekitar 100.000 kali sehari.",
    "Info: Lampu pijar ditemukan oleh Thomas Edison pada tahun 1879."
]

def tampilkan_informasi_acak():
    info = random.choice(info_acak)
    messagebox.showinfo("Informasi Acak", info)

# Membuat jendela utama
root = tk.Tk()
root.title("Informasi Acak")

# Membuat tombol sebagai kotak-kotak
kotak = []
for i in range(5):
    button = tk.Button(root, text=f"Garisan {i+1}", command=tampilkan_informasi_acak, width=10, height=5)
    button.grid(row=0, column=i, padx=5, pady=5)
    kotak.append(button)

# Menjalankan loop aplikasi
root.mainloop()
