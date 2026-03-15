# cau2
import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if a == 0:
    if b == 0:
        print("Vô nghiệm")
    else:
        print("x =", -c/b)
else:
    delta = b*b - 4*a*c
    print("delta", delta)
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        print("x =", -b/(2*a))
    else:
        print("x1 =", (-b + math.sqrt(delta))/(2*a))
        print("x2 =", (-b - math.sqrt(delta))/(2*a))
#cau4
n = int(input("Nhập n: "))
if n < 0:
    n = -n
hang_tram = (n // 100) % 10

print("Chữ số hàng trăm:", hang_tram)
#cau6 
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
#cau8
tnct = int(input("Nhập thâm niên ( số tháng đã làm ): ")) 
luong_cb = 1350000

if tnct < 12:
    hs = 2.34
elif tnct < 36:
    hs = 3.33
elif tnct < 60:
    hs = 3.66
else:
    hs = 3.99

luong = hs * luong_cb

print("Lương:", luong, "đồng")
#cau10
gio = int(input("Nhập số giờ thuê: "))
gio_batdau = int(input("Nhập giờ bắt đầu: "))

if gio <= 3:
    tien = gio * 100000
else:
    tien = 3*100000 + (gio-3)*75000

if 11 <= gio_batdau <= 15:
    tien = tien * 0.9

print("Tiền thuê sân:", tien)
#cau12
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang == 2:
    max = 28
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    max = 30
else:
    max = 31

if ngay < max:
    ngay += 1
else:
    ngay = 1
    if thang == 12:
        thang = 1
    else:
        thang += 1

print("Ngày tiếp theo:", ngay, "/", thang)
