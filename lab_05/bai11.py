s = input("Nhập chuỗi nhị phân: ")
tong = 0
mu = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == '1':
        tong += 2**mu
    mu += 1
print("Thập phân: ", tong)


