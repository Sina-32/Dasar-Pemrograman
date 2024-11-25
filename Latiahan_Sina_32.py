'''
Nama: Sina Pijar Sahmura
Nim: 2400606
Kelas: 1B
'''
search = 20
array_list = [10, 15, 30, 70, 80, 60, 20, 90]

def linear_search(search, array_list):
    
    for item in array_list:
        if item == search:
            return True
    return False

if linear_search(search, array_list):
    print('Ditemukan')
else:
    print('Tidak Ditemukan')

search = 20
array_list = [10, 15, 30, 70, 80, 60, 20, 90]

def linear_search(search, array_list):
    
    for item in array_list:
        if item == search:
            return True
    return False

result = linear_search(search, array_list)

if result > 0:
    print('Ditemukan')
else:
    print('Tidak Ditemukan')



