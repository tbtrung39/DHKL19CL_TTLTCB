s = input("Nhập chuỗi: ")
dem = 0
for char in s:
    if not char.isalnum(): 
        dem += 1
print(f"Số ký tự đặc biệt: {dem}")