n = int(input("Nhap n cho bai 1 : "))
tong = 1.0
tich = 1.0 
for i in range(1, n + 1):
    tich *= (2 * i) / (2 * i + 1)
    tong += tich
print(f"Ket qua bai 1: {round(tong, 3)}")