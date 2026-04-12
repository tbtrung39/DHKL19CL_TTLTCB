m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
tong_ma_tran = 0
print("Nhập các phần tử cho ma trận A:")
for i in range(m):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"Nhập a[{i}][{j}]: "))
        hang.append(gia_tri)
        tong_ma_tran = tong_ma_tran + gia_tri   
    A.append(hang)
print("\n--- KẾT QUẢ ---")
print("a. Ma trận A vừa nhập là:")
for hang in A:
    print(hang)
print(f"b. Tổng các phần tử của Ma trận A là: {tong_ma_tran}")