#2
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình bậc nhất, nghiệm x =", x)

else:
    delta = b*b - 4*a*c
    
    if delta < 0:
        print("Phương trình vô nghiệm")
        
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép x =", round(x,2))
        
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("x1 =", round(x1,2))
        print("x2 =", round(x2,2))

#4
n = int(input("Nhập số nguyên: "))

n = abs(n)   # tránh số âm

hangtram = (n // 100) % 10

print("Chữ số hàng trăm là:", hangtram)

#6
n = int(input("Nhập số có 3 chữ số: "))

tram = n // 100
chuc = (n // 10) % 10
donvi = n % 10

so = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]

print(so[tram], "trăm", so[chuc], "mươi", so[donvi])

#8
luong_cb = 1350000

tnct = int(input("Nhập thâm niên công tác (tháng): "))

if tnct < 12:
    heso = 2.34
elif tnct < 36:
    heso = 3.33
elif tnct < 60:
    heso = 3.66
else:
    heso = 3.99

luong = heso * luong_cb

print("Lương nhân viên =", luong)

#10
gio = int(input("Nhập số giờ thuê sân: "))

gia_3gio_dau = 100000
gia_sau = gia_3gio_dau * 0.75

if gio <= 3:
    tien = gio * gia_3gio_dau
else:
    tien = 3 * gia_3gio_dau + (gio - 3) * gia_sau

# giảm giá khung giờ 11-15
if 11 <= gio <= 15:
    tien = tien * 0.9

print("Tiền thuê sân =", tien)

#12
# nhập ngày tháng năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# số ngày của từng tháng (năm không nhuận)
songay = [31,28,31,30,31,30,31,31,30,31,30,31]

# kiểm tra ngày hợp lệ
if ngay < songay[thang-1]:
    ngay += 1
else:
    ngay = 1
    if thang < 12:
        thang += 1
    else:
        thang = 1
        nam += 1

print("Ngày tiếp theo là:", ngay, "/", thang, "/", nam)