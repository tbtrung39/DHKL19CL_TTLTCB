a = []
print("Nhập các số tự nhiên (nhập 0 để dừng):")
while True:
    x = input("Nhập số: ")
    x = int(x)
    if x == 0:
        break
    a.append(x)

# Chèn danh sách [1, 2, 3] vào vị trí đầu,cuối và thứ 5
a_copy = a[:]
a_copy = [1, 2, 3] + a_copy
a_copy = a_copy + [1, 2, 3]
if len(a_copy) >= 5:
    a_copy[4:4] = [1, 2, 3]
else:
    a_copy = a_copy + [1, 2, 3]
print("Danh sách sau khi chèn: ", a_copy)

# Xóa phần tử thứ k
k = input("Nhập vị trí k để xóa phần tử: ")
k = int(k)
a_xoa = a[:]
if 0 <= k < len(a_xoa):
    a_xoa.pop(k)
    print(f"Danh sách sau khi xóa phần tử tại vị trí {k}: ", a_xoa)
else:
    print("Vị trí k không hợp lệ.")

# Sắp xếp tăng dần và giảm dần
a_tang = sorted(a)
a_giam = sorted(a, reverse=True)
print("Danh sách sau khi sắp xếp tăng dần: ", a_tang)
print("Danh sách sau khi sắp xếp giảm dần: ", a_giam)