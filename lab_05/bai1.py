s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if c.isdigit():
        dem += 1
print("Số ký tự là số: ", dem)