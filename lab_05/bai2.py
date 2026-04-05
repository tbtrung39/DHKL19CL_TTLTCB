s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if not c.isalpha() and not c.isdigit():
        dem += 1
print("Số ký tự đặc biệt: ", dem)