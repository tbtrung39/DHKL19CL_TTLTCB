str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
kq = ""
for i in range(max(len(str1), len(str2))):
    if i < len(str1):
        kq = kq + str1[i]
    if i < len(str2):
        kq = kq + str2[i]
print(kq)