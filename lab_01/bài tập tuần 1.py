# Bài 1
masv = input("Nhập mã sinh viên: ")
hoten = input("Nhập họ tên: ")
quequan = input("Nhập quê quán: ")
namsinh = int(input("Nhập năm sinh: "))
dtb = float(input("Nhập điểm trung bình: "))

print("\nThông tin sinh viên:")
print("Mã SV:", masv)
print("Họ tên:", hoten)
print("Quê quán:", quequan)
print("Năm sinh:", namsinh)
print("Điểm TB:", dtb)

# Bài 2
t = int(input("Nhập số giây: "))
d = t // 86400
t = t % 86400
h = t // 3600
t = t % 3600
m = t // 60
s = t % 60
print(d,"ngày,",h,"giờ,",m,"phút,",s,"giây")

# Bài 3
import math
r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))
pi = 3.14
Sxq = 2*pi*r*h
Stp = Sxq + 2*pi*r*r
V = pi*r*r*h
print(f"Diện tích xung quanh: {Sxq:.2f}")
print(f"Diện tích toàn phần: {Stp:.2f}")
print(f"Thể tích: {V:.2f}")

# Bài 4
import math
x = float(input("Nhập x: "))
F = (-x + math.sqrt(x**2 + 4)) / (7 * math.sqrt(x**4 + 1))
print(f"Kết quả: {F:.2f}")

# Bài 5
a1 = float(input("Nhập a1: "))
a2 = float(input("Nhập a2: "))
a3 = float(input("Nhập a3: "))
b1 = float(input("Nhập b1: "))
b2 = float(input("Nhập b2: "))
b3 = float(input("Nhập b3: "))
tich = a1*b1 + a2*b2 + a3*b3
print("Tích vô hướng là :", tich)

# Bài 6
t = float(input("Nhập thời gian sử dụng (giây): "))
dien_nang = (200*2.7) * t / 3600000
tien = dien_nang * 7000
print(f"Tiền điện phải trả : {tien:.2f} đồng")

# Bài 7
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
x = -b/(2*a)
y = a*x*x + b*x + c
print(f"Đỉnh của pt bậc 2 là : ({x:.2f},{y:.2f})")

# Bài 8
x1,y1 = map(float,input("Nhập A: ").split())
x2,y2 = map(float,input("Nhập B: ").split())
x3,y3 = map(float,input("Nhập C: ").split())
gx = (x1+x2+x3)/3
gy = (y1+y2+y3)/3
print(f"Trọng tâm G :({gx:.2f},{gy:.2f})")

# Bài 9
x,y,z = map(float,input("Nhập tọa độ điểm: ").split())
print("Đối xứng qua Oxy là:",x,y,-z)
print("Đối xứng qua Oxz là:",x,-y,z)
print("Đối xứng qua Oyz là:",-x,y,z)

# Bài 10
import math
x = float(input("Nhập x: "))
F = math.log(x,4) + math.log(2,x)
print(f"Kết quả là:{F:.2f}")

# Bài 11
P = 1 - (5/6)**3
print(f"Xác suất ít nhất 1 lần ra 6 là:{P:.2f}")

# Bài 12
import math
a = float(input("Nhập vận tốc a: "))
t = (a**4) / (math.log(5,4))
print(f"Thời gian xe dừng là:{t:.2f}")