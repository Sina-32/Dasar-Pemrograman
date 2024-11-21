'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
print("Bogo Sort")
def is_sorted(arr):
    return arr == sorted(arr)

def bogo_sort(arr):
    while not is_sorted(arr):
        arr.sort(reverse=True) 
    return arr

arr = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

print(f"Sebelum diurutkan: {arr}")

bogo_sort(arr)

print(f"Setelah diurutkan: {arr}")

import time

# Catat waktu mulai
start_time = time.time()

# Kode yang ingin diukur waktunya
for i in range(1000000):
    pass

# Catat waktu selesai
end_time = time.time()

# Hitung selisih waktu
execution_time = end_time - start_time

# Format output dengan 4 angka di belakang koma
print(f"Waktu Eksekusi: {execution_time:.4f}")
