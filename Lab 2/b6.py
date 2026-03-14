n = int(input("Nhập số nguyên có 3 chữ số: "))
if 100 <= n <= 999:
    tram = n // 100
    chuc = (n % 100) // 10
    donvi = n % 10
    so = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
    print(so[tram], "trăm", end=" ")
    if chuc == 0:
        if donvi != 0:
            print("linh", so[donvi])
    elif chuc == 1:
        print("mười", end=" ")
        if donvi != 0:
            print(so[donvi])
    else:
        print(so[chuc], "mươi", end=" ")
        if donvi != 0:
            print(so[donvi])
else:
    print("Số không hợp lệ")