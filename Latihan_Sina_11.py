'''
Nama : Sina
Nim : 2400606
Kelas : 1B
'''
student={
    'Alice':'Computer Science',
    'Bob':'Matematics',
    'Charlie':'Physics',
    'David': 'Computer Science',
    'Eva': 'Matematics'
}
print(f"Computer Science sebanyak",list(student.values()).count('Computer Science'))
print(f"Matematics sebanyak",list(student.values()).count('Matematics'))
print(f"Physics sebanyak sebanyak",list(student.values()).count('Physics'))