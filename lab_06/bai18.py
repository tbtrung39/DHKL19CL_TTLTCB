# Nhập ma trận
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
A = []
for i in range(m):
    row = list(map(int, input(f"Nhập hàng {i}: ").split()))
    A.append(row)
# Tính tổng các phần tử của ma trận A
tong = 0
for row in A:
    tong += sum(row)
print("Tổng:", tong)
