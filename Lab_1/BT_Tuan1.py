#cau1
mssv = input("Nhập mã số sinh viên: ")
hoten = input("Nhập họ tên: ")
quequan = input("Nhập quê quán: ")
namsinh = int(input("Nhập năm sinh: "))
dtb = float(input("Nhập điểm trung bình: "))
print("\nThông tin sinh viên:")
print("MSSV:", mssv)
print("Họ tên:", hoten)
print("Quê quán:", quequan)
print("Năm sinh:", namsinh)
print("Điểm trung bình:", dtb)
#cau2
t = int(input("Nhập số giây: "))
d = t // 86400
t = t % 86400
h = t // 3600
t = t % 3600
m = t // 60
s = t % 60
print(d,"ngày",h,"giờ",m,"phút",s,"giây")
#cau3
import math
x = float(input("Nhập x: "))
f = (-x + math.sqrt(x**2 + 4)) / (7 * math.sqrt(x**4 + 1))
print("Giá trị f(x) =", round(f,2))
#cau4
a1 = float(input("a1: "))
a2 = float(input("a2: "))
a3 = float(input("a3: "))
b1 = float(input("b1: "))
b2 = float(input("b2: "))
b3 = float(input("b3: "))
dot = a1*b1 + a2*b2 + a3*b3
print("Tích vô hướng =", dot)
#cau5
U = 220
I = 2.7
t = float(input("Nhập thời gian dùng (giây): "))
P = U * I
A = P * t
kwh = A / 3600000
tien = kwh * 7000
print("Tiền điện =", round(tien,2),"đồng")
#cau6
import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
delta = b*b - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b/(2*a)
    print("Nghiệm kép:", round(x,2))
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)

    print("x1 =", round(x1,2))
    print("x2 =", round(x2,2))
#cau7
xA = float(input("xA: "))
yA = float(input("yA: "))
xB = float(input("xB: "))
yB = float(input("yB: "))
xC = float(input("xC: "))
yC = float(input("yC: "))
xG = (xA + xB + xC)/3
yG = (yA + yB + yC)/3
print("Trọng tâm G(", round(xG,2), ",", round(yG,2), ")")
#cau8
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
print("Đối xứng qua Oxy:", x, y, -z)
print("Đối xứng qua Oxz:", x, -y, z)
#cau9
import math
x = float(input("Nhập x: "))
f = math.log(x,4) + math.log(2,x)
print("f(x) =", round(f,2))
#cau10
p = 1 - (5/6)**3
print("Xác suất =", round(p,2))
#cau11
import math
a = float(input("Nhập a: "))
t = float(input("Nhập thời gian t: "))
v = -t * math.log(5 + 4*a, 4)
print("Vận tốc =", round(v,2))