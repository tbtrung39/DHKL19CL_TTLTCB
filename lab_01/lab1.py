#bai1
msv = input("Nhập mã số sinh viên: ")
ho_ten = input("Nhập họ tên: ")
que_quan = input("Nhập quê quán: ")
nam_sinh = int(input("Nhập năm sinh: "))
diem_tb = float(input("Nhập điểm trung bình: "))

print("\n--- Thông tin sinh viên vừa nhập ---")
print(f"MSV: {msv} | Họ tên: {ho_ten} | Quê quán: {que_quan}")
print(f"Năm sinh: {nam_sinh} | Điểm TB: {diem_tb}")
#bai2
s_tong = int(input("Nhập số giây: "))

d = s_tong // (24 * 3600)
s_con_lai = s_tong % (24 * 3600)
h = s_con_lai // 3600
s_con_lai %= 3600
m = s_con_lai // 60
s = s_con_lai % 60

print(f"Kết quả: {d} ngày, {h} giờ, {m} phút, {s} giây")
#b
r = float(input("Nhập bán kính r: "))
h = float(input("Nhập chiều cao h: "))
pi = 3.14

s_xung_quanh = 2 * pi * r * h
s_toan_phan = s_xung_quanh + 2 * pi * (r**2)
the_tich = pi * (r**2) * h

print(f"S xung quanh: {s_xung_quanh:.2f}, S toàn phần: {s_toan_phan:.2f}, Thể tích: {the_tich:.2f}")
#bai3
import math
x = float(input("Nhập x: "))

tu_so = -x + math.sqrt(x**2 + 4)
mau_so = (x**4 + 1)**(1/7)
f_x = tu_so / mau_so

print(f"Giá trị f(x) = {f_x:.2f}")
#bai4
ax, ay = map(float, input("Nhập tọa độ vector a (x y): ").split())
bx, by = map(float, input("Nhập tọa độ vector b (x y): ").split())

tich_vo_huong = ax * bx + ay * by
print(f"Tích vô hướng của 2 vector là: {tich_vo_huong:.2f}")
#bai5
u = 220 # Hiệu điện thế
i = 2.7 # Cường độ dòng điện
gia_dien = 7000 # đ/kWh

t_giay = float(input("Nhập thời gian sử dụng (giây): "))

# Công thức: P = U * I (Watt), Điện năng A = P * t (Joule)
# Đổi Joule sang kWh: 1 kWh = 3,600,000 Joule
p_watt = u * i
a_joule = p_watt * t_giay
a_kwh = a_joule / 3600000

tien_dien = a_kwh * gia_dien
print(f"Tiền điện phải trả: {tien_dien:.2f} đ")
#bai6
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    print(f"Nghiệm x = {-c/b:.2f}" if b != 0 else "PT vô nghiệm")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        print(f"Nghiệm kép x = {-b/(2*a):.2f}")
    else:
        print("Phương trình vô nghiệm")
#bai7
x1, y1 = map(float, input("Tọa độ A (x y): ").split())
x2, y2 = map(float, input("Tọa độ B (x y): ").split())
x3, y3 = map(float, input("Tọa độ C (x y): ").split())

xg = (x1 + x2 + x3) / 3
yg = (y1 + y2 + y3) / 3

print(f"Trọng tâm G có tọa độ: ({xg:.2f}, {yg:.2f})")
#bai8
x, y, z = map(float, input("Nhập tọa độ điểm M(x y z): ").split())

print(f"Đối xứng qua Oxy: ({x}, {y}, {-z})")
print(f"Đối xứng qua Oxz: ({x}, {-y}, {z})")
print(f"Đối xứng qua Oyz: ({-x}, {y}, {z})")
#bai9
import math
x = float(input("Nhập x (x > 0 và x != 1): "))

f_x = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x))
print(f"Giá trị f(x) = {f_x:.2f}")
#bai10
n = int(input("Nhập số lần tung n: "))
p = 1 - (5/6)**n
print(f"Xác suất ít nhất 1 lần ra mặt 6 là: {p:.2f}")
#bai11
import math
a = float(input("Nhập giá trị a: "))

# Để v(t) = 0 => -t * log4(5) + a^4 = 0
# t = a^4 / log4(5)
log4_5 = math.log(5) / math.log(4)
t = (a**4) / log4_5

print(f"Thời gian ô tô đi được đến lúc dừng: {t:.2f} giây")
