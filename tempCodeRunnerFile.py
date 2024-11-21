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