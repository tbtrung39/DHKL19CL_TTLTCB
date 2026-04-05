s = input("Nhập chuỗi: ")
# Thay dấu phẩy bằng khoảng trắng
s = s.replace(",", " ")
words = s.split()
for w in words:
    print(w)
    