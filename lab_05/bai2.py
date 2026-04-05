str_input = input("Nhập vào một chuỗi: ")
dem = 0
for i in str_input:
    if not (i.isdigit() or i.isalpha()):
        dem = dem + 1
print("Số ký tự không phải số và không phải chữ là:", dem)