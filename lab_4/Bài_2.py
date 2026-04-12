n = int(input("Nhập số lượng số hạng n: "))
sa = sb = sc = 0

for i in range(1, n + 1):
    sa += ((-1)**(i+1)) * (1/i)
    sb += 1 / (i * (i + 1))
    sc += 1 / (i + 1)**0.5

print(f"Sa={sa:.3f}, Sb={sb:.3f}, Sc={sc:.3f}")