s = input("Nhập chuỗi: ")
dem = 0
for char in s:
    if char.isdigit():
        dem += 1
print(f"Số lượng ký tự là số: {dem}")