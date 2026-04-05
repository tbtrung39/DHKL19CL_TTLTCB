Str1 = input("Nhập chuỗi: ")
Str1 = Str1.replace(",", " ")
danh_sach = Str1.split()
for tu in danh_sach:
    print(tu)