"""
#Bai1:
masv = input("Nhap ma sinh vien: ")
hoten = input("Nhap ho ten: ")
quequan = input("Nhap que quan: ")
namsinh = int(input("Nhap nam sinh: "))
diemtb = float(input("Nhap diem trung binh: "))
print("Thong tin sinh vien:")
print("Ma SV:", masv)
print("Ho ten:", hoten)
print("Que quan:", quequan)
print("Nam sinh:", namsinh)
print("Diem trung binh:", diemtb)
"""
"""
#Bai2:
s = int(input("Nhap so giay: "))
m = int(input("Nhap so phut: "))
h = int(input("Nhap so gio: "))
d = int(input("Nhap so ngay: "))
print(d, "ngay", h, "gio", m, "phut", s, "giay")
"""
"""
#Bai3:
import math

x = float(input("Nhap x: "))
tu = -x + math.sqrt(x**2 + 4)
mau = (x**4 + 1)**(1/7)
f = tu / mau 
print("Gia tri f(x) =", round(f,2))
"""
"""
#Bai4:
print("Nhap vector a")
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

print("Nhap vector b")
b1 = float(input("b1 = "))
b2 = float(input("b2 = "))
b3 = float(input("b3 = "))

tich = a1*b1 + a2*b2 + a3*b3
print("Tich vo huong =", tich)
"""
"""
#Bai5:
U = 220
I = 2.7

t = float(input("Nhap thoi gian su dung (giay): "))
P = U * I
E = P * t
E_kwh = E / 3600000
tien = E_kwh * 7000
print("Tien dien =", round(tien,2), "dong")
"""
"""
#Bai6:
import math
a, b, c = map(float, input("Nhap a b c: ").split())
delta = b*b - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    x = -b/(2*a)
    print("Nghiem kep:", round(x,2))
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)   
    print("x1 =", round(x1,2))
    print("x2 =", round(x2,2))
"""
"""
#Bai7
x1, y1 = map(float, input("Nhap toa do A (x1 y1): ").split())
x2, y2 = map(float, input("Nhap toa do B (x2 y2): ").split())
x3, y3 = map(float, input("Nhap toa do C (x3 y3): ").split())
xg = (x1 + x2 + x3) / 3
yg = (y1 + y2 + y3) / 3
print("Trong tam G(", round(xg,2), ",", round(yg,2), ")")
"""
"""
#Bai8:
x, y, z = map(float, input("Nhap toa do diem (x y z): ").split())
print("Doi xung qua Oxy:", x, y, -z)
print("Doi xung qua Oxz:", x, -y, z)
print("Doi xung qua Oyz:", -x, y, z)
"""
"""
#Bai9:
import math
x = float(input("Nhap x: "))
f = math.log(x,4) + math.log(2,x)
print("f(x) =", round(f,2))
"""
"""
#Bai10:
n = int(input("Nhap n: "))
p = 1 - (1 - (1/6)**3)**n
print("Xac suat =", round(p,2))
"""
"""
#Bai 11:
import math
a = float(input("Nhap van toc a: "))
t = (a**4) / (math.log(5,4))
print("Thoi gian xe dung =", round(t,2))
"""