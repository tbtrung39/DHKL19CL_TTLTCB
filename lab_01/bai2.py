import math

d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
tong_giay = d*86400 + h*3600 + m*60 + s
print(f"Tổng cộng: {tong_giay} giây")

pi = 3.14
r = float(input("Nhập bán kính r: "))
h_tru = float(input("Nhập chiều cao h: "))

s_xq = 2 * pi * r * h_tru
s_tp = s_xq + 2 * pi * (r**2)
the_tich = pi * (r**2) * h_tru

print(f"Diện tích xung quanh: {round(s_xq, 2)}")
print(f"Diện tích toàn phần: {round(s_tp, 2)}")
print(f"Thể tích: {round(the_tich, 2)}")