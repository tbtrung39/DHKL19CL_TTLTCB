s = int(input("Nhập giây: "))
m = int(input("Nhập phút: "))
h = int(input("Nhập giờ: "))
d = int(input("Nhập ngày: "))

giay = s + m*60 + h*3600 + d*86400

d = giay // 86400
h = (giay % 86400) // 3600
m = (giay % 3600) // 60
s = giay % 60
print("Thời gian:", d, "ngày,", h, "giờ,", m, "phút,", s, "giây")


#Ý thứ hai
r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))
pi = 3.14
Sxq = 2 * pi * r * h
Stp = 2 * pi * r * (h + r)
V = pi * r * r * h

print("Diện tích xung quanh:", round(Sxq, 2))
print("Diện tích toàn phần:", round(Stp, 2))
print("Thể tích:", round(V, 2))