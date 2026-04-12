m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = [[int(input(f"a[{i+1}][{j+1}]: ")) for j in range(n)] for i in range(m)]
print("Ma trận A:")
for row in A:
    print(row)

tong = sum(A[i][j] for i in range(m) for j in range(n))
print("Tổng các phần tử:", tong)