#1 
masv = input("Nhập mã sinh viên: ")
hoten = input("Nhập họ tên: ")
quequan = input("Nhập quê quán: ")
namsinh = int(input("Nhập năm sinh: "))
dtb = float(input("Nhập điểm trung bình: "))
print("\nTHÔNG TIN SINH VIÊN")
print("Mã SV:", masv)
print("Họ tên:", hoten)
print("Quê quán:", quequan)
print("Năm sinh:", namsinh)
print("Điểm TB:", dtb)

#2
s = int(input("Nhập số giây: "))

d = s // 86400
s = s % 86400

h = s // 3600
s = s % 3600

m = s // 60
s = s % 60

print("Kết quả:", d, "ngày", h, "giờ", m, "phút", s, "giây")

#3
import math

x = float(input("Nhập x: "))

f = (-x + math.sqrt(x**2 + 4)) / ((x**4 + 1) ** (1/7))

print("Giá trị f(x) =", round(f,2))

#4
print("Nhập vector a")
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

print("Nhập vector b")
b1 = float(input("b1 = "))
b2 = float(input("b2 = "))
b3 = float(input("b3 = "))

tich = a1*b1 + a2*b2 + a3*b3

print("Tích vô hướng =", tich)

#5
U = 220
I = 2.7

t = float(input("Nhập thời gian sử dụng (giây): "))

P = U * I  # công suất W

# đổi sang kWh
diennang = P * t / (1000 * 3600)

tien = diennang * 7000

print("Tiền điện phải trả =", round(tien,2), "đ")

#6
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Phương trình vô nghiệm")

elif delta == 0:
    x = -b/(2*a)
    print("Nghiệm kép x =", round(x,2))

else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("x1 =", round(x1,2))
    print("x2 =", round(x2,2))

#7
xA = float(input("xA = "))
yA = float(input("yA = "))

xB = float(input("xB = "))
yB = float(input("yB = "))

xC = float(input("xC = "))
yC = float(input("yC = "))

xG = (xA + xB + xC) / 3
yG = (yA + yB + yC) / 3

print("Trọng tâm G =", (round(xG,2), round(yG,2)))

#8
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

print("Đối xứng qua Oxy:", (x, y, -z))
print("Đối xứng qua Oxz:", (x, -y, z))
print("Đối xứng qua Oyz:", (-x, y, z))

#9
import math

x = float(input("Nhập x: "))

f = math.log(x,4) + math.log(2,x)

print("f(x) =", round(f,2))

#10
n = int(input("Nhập số lần tung xúc xắc: "))

p = 1 - (5/6)**n

print("Xác suất =", round(p,2))

#11
import math

a = float(input("Nhập vận tốc ban đầu a: "))

t = (a**4) / (math.log(5,4))

print("Thời gian xe dừng =", round(t,2))
