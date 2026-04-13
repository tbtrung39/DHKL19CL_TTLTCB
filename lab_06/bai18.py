m = input("Nhập số hàng: ")
m = int(m)
n = input("Nhập số cột: ")
n = int(n)
A = []
for i in range(m):
    row = list(map(int, input(f"Hàng {i}: ").split()))
    A.append(row)
# tính tổng
tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]
print("Tổng ma trận:", tong)