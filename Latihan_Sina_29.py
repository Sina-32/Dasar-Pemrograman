'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''

print("Merge Sort")
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedleft = merge_sort(leftHalf)
    sortedright = merge_sort(rightHalf)

    return merge(sortedleft, sortedright)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])

    result.extend(right[j:])
    
    return result

unsortedArr = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 
               59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 
               60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 
               5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

sortedArr = merge_sort(unsortedArr)

print(f"sebelum diurutkan {unsortedArr}")
print(f"Setela diurutkan {sortedArr}")

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

