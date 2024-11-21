'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
print("Quick Sort")
def quick_sort(arr):
    if len(arr) <= 1: 
        return arr
    
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot] 
    
    return quick_sort(left) + middle + quick_sort(right)

unsortedarr = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 
               59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 
               60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 
               5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

print(f"sebelum diurutkan {unsortedarr}")

sortedarr = quick_sort(unsortedarr)

print(f"Setela diurutkan {sortedarr}")


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
