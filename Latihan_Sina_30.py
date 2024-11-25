'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
print("Counting Sort")
def counting_sort(arr):

    max_val = max(arr)
    min_val = min(arr)
    
    count = [0] * (max_val - min_val + 1)
    
    for num in arr:
        count[num - min_val] += 1
    
    arr[:] = [i + min_val for i, c in enumerate(count) for _ in range(c)]

arr = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 
       59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 
       60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 
       5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

print(f"Sebelum diurutkan: {arr}")

counting_sort(arr)

print(f"Setelah diurutkan: {arr}")

import time

# Catat waktu mulai
start_time = time.perf_counter()

# Kode yang ingin diukur waktunya
for i in range(1000000):
    pass

# Catat waktu selesai
end_time = time.perf_counter()

# Hitung selisih waktu
execution_time = end_time - start_time

# Format output dengan 4 angka di belakang koma
print(f"Waktu Eksekusi: {execution_time:.4f}")