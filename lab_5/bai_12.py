str1 = input("Nhập chuỗi: ")
tu_list = str1.replace(',', ' ').split()
for tu in tu_list:
    print(tu)