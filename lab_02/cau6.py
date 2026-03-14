n = int(input("Nhập số có 3 chữ số: "))

tram = n // 100
chuc = (n // 10) % 10
donvi = n % 10

so = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]

print(so[tram], "trăm", end=" ")

if chuc == 0 and donvi != 0:
    print("lẻ", so[donvi])
elif chuc == 0 and donvi == 0:
    print()
else:
    if donvi == 0:
        print(so[chuc], "mươi")
    else:
        print(so[chuc], "mươi", so[donvi])