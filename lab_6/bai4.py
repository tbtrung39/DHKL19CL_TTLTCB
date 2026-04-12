a = []
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0: break
    a.append(n)

sub = [1, 2, 3]
# Chèn danh sách con (Dùng slicing để chèn cả list vào)
a = sub + a                       
a = a + sub                       
if len(a) >= 5:
    a[4:4] = sub                  
print("Sau khi chèn [1,2,3]:", a)

# Xóa phần tử thứ k
k = int(input("Nhập vị trí k cần xóa (bắt đầu từ 0): "))
if 0 <= k < len(a):
    a.pop(k)
    print(f"Sau khi xóa vị trí {k}:", a)

# Sắp xếp
print("Tăng dần:", sorted(a))
print("Giảm dần:", sorted(a, reverse=True))