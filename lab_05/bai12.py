s = input("Nhập chuỗi: ")
s = s.replace(",", "")
words = s.split()       
for w in words:
    print(w)