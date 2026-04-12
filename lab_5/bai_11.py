s = input("Nhập chuỗi nhị phân: ")
try:
    thap_phan = int(s, 2)
    print(f"Giá trị thập phân: {thap_phan}")
except ValueError:
    print("Đây không phải chuỗi nhị phân hợp lệ.")