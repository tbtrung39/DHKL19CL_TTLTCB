a = []
while True:
    x = int(input("Nhập số ( 0 để dừng ): "))
    if x == 0:
        break
    a.append(x)
# Chèn [1,2,3] vào vị trí đầu, cuối và vị trí thứ 5 của danh sách
a = [1,2,3] + a    # Đầu
a = a + [1,2,3]    # Cuối
if len(a) >= 5:
    a = a[:4] + [1,2,3] + a[4:]
print(a)
# Xoá phần tử thứ k trong danh sách
k = int(input("Nhập k: "))
if 0 <= k < len(a):
    a.pop(k)
print(a)
# Sắp xếp theo thứ tự tăng, giảm dần
print("Tăng dần: ", sorted(a))
print("Giảm dần: ", sorted(a, reverse=True))
