'''
Nama : Sina Pijar Sahmura
Nim : 2400606
Kelas : 1B
'''
import numpy as np

suhu_celsius = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
suhu_fahrenheit = (suhu_celsius * 9/5) + 32

print(f"Suhu dalam Celsius selama 10 hari terakhir: {suhu_celsius}")
print(f"Suhu dalam Fahrenheit selama 10 hari terakhir: {suhu_fahrenheit}")
