import random

n = int(input("Nhập số tự nhiên n: "))

day_A = list(range(1, n + 1))
ket_qua = []

while len(day_A) > 0:
    so_ngau_nhien = random.choice(day_A)
    
    ket_qua.append(so_ngau_nhien)
    
    day_A.remove(so_ngau_nhien)

print("Dãy result sau khi thiết lập là:", ket_qua)