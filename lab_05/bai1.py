str_input = input("Nhập vào một chuỗi: ")
dem = 0
for i in str_input:
    if i.isdigit():
        dem = dem + 1
print("Số ký tự là số trong chuỗi là:", dem)