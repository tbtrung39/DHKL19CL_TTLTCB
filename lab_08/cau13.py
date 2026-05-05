def la_nam_nhuan(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return True
    else:
        return False
def so_ngay_trong_thang(n, x):
    if n in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif n in [4, 6, 9, 11]:
        return 30
    elif n == 2:
        if la_nam_nhuan(x):
            return 29
        else:
            return 28
    else:
        return "Thang khong hop le"
y = input("Nhap vao nam: ")
y = int(y)
m = input("Nhap vao thang: ")
m = int(m)
if la_nam_nhuan(y):
    print(y,"la nam nhuan.")
else:
    print(y,"khong la nam nhuan.")
print("So ngay trong thang:", so_ngay_trong_thang(m, y))