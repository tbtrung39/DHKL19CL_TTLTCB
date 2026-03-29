n = int(input("Nhập số: "))
tong = 0
while n > 0:
    tong += n % 10
    n = n // 10
print(f"Tổng là: {tong}")