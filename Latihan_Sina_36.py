'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]

search = 60

def linear_search(search, array_list):
    for item in array_list:
        if item == search:
            return True
    return False

def binary_search(search, array_list):
    left = 0
    right = len(array_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if array_list[mid] == search:
            return mid
        elif array_list[mid] < search:
            left = mid + 1
        else:
            right = mid - 1

import time

start_time = time.perf_counter()
linear_result = linear_search(search, array)
end_time = time.perf_counter()
linear_time = end_time - start_time

start_time = time.perf_counter()
binary_result = binary_search(search, array)
end_time = time.perf_counter()
binary_time = end_time - start_time

print(f"Waktu Linear Search: {linear_time:.7f} detik")
print(f"Waktu Binary Search: {binary_time:.7f} detik")

