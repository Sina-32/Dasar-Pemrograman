'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
arr = [2, 5, 8, 12, 23, 38, 56, 72, 91]
search = 23

def binary_search(search, array_list):
    left = 0
    right = len(array_list)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == search:
            return mid
        elif search > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

result = binary_search(search, arr)
print(f'pencarian23: {result}') 

arr = [2, 5, 8, 91, 23, 38, 56, 72, 12]
search = 23

def binary_search(search, array_list):
    array_list.sort()
    left = 0
    right = len(array_list)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == search:
            return mid
        elif search > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

result = binary_search(search, arr)
print(f'pencarian23: {result}') 