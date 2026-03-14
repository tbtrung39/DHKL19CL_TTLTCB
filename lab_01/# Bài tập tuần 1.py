# Bài tập tuần 1
# Bài 1: Nhập thông tin sinh viên và in ra:
masv = input("Nhập mã sinh viên: ")
hoten = input("Nhập họ tên: ")
quequan = input("Nhập quê quán: ")
namsinh = int(input("Nhập năm sinh: "))
diemtb = float(input("Nhập điểm trung bình: "))
print("-" * 20)
print(f"Thông tin SV: {hoten} ({masv})")
print(f"Quê quán: {quequan} | Năm sinh: {namsinh}")
print(f"Đểm TB: {diemtb}")

#=================================
# Bài 2: Nhập số giây, phút, giờ, ngày và in ra kết quả:
s = input("Nhập giây: ")
m = input("Nhập phút: ")
h = input("Nhập giờ: ")
d = input("Nhập ngày: ")
print(f"Kết quả: {d} ngày, {h} giờ, {m} phút, {s} giây")

#=================================
# Bài 3: Nhập x, tính f(x):
import math
x = float(input("Nhập x: "))
tu_so = -x + math.sqrt(x**2 + 4)
mau_so = (x**4 + 1)**(1/7)
f = tu_so / mau_so
print(f"Giá trị f({x}) = {f:.2f}")

#=================================
# Bài 4: Tính tích vô hướng:
print("Nhập vector a (3 số cách nhau khoảng trắng):")
a = list(map(float, input().split()))
print("Nhập vector b (3 số cách nhau khoảng trắng):")
b = list(map(float, input().split()))
tich_vo_huong = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(f"Tích vô hướng = {tich_vo_huong}")

#=================================
# Bài 5: Tính tiền điện:
U, I = 220, 2.7
thoi_gian_giay = float(input("Nhập thời gian sử dụng (giây): "))
cong_suat_W = U * I
nang_luong_J = cong_suat_W * thoi_gian_giay
# Đổi từ Joule sang kWh: 1 kWh = 3,600,000 J
so_dien_kwh = nang_luong_J / 3600000
tong_tien = so_dien_kwh * 7000
print(f"Tiền điện phải trả: {tong_tien:,.2f} đồng")

#=================================
# Bài 6: Giải phương trình bậc 2:
import math
a, b, c = map(float, input("Nhập a, b, c: ").split())
if a == 0:
    print("Đây không phải phương trình bậc 2 (a phải khác 0)")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print(f"Nghiem kép: x = {-b/(2*a):.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Có 2 nghiệm: x1 = {x1:.2f}, x2 = {x2:.2f}")

#=================================
# Bài 7: Trọng tâm:
ax, ay = map(float, input("Tọa độ A: ").split())
bx, by = map(float, input("Tọa độ B: ").split())
cx, cy = map(float, input("Tọa độ C: ").split())
print(f"Trọng tâm G({(ax+bx+cx)/3:.2f}, {(ay+by+cy)/3:.2f})")

#=================================
# Bài 8: Đối xứng:
x, y, z = map(float, input("Nhập x y z: ").split())
print(f"Qua Oxy: ({x}, {y}, {-z})")
print(f"Qua Oxz: ({x}, {-y}, {z})")
print(f"Qua Oyz: ({-x}, {y}, {z})")

#=================================
# Bài 9: Tính log:
import math
x = float(input("Nhập x: "))
if x > 0 and x != 1:
    f = math.log(x, 4) + math.log(2, x)
    print(f"f(x) = {f:.2f}")
else:
    print("x phải dương và khác 1")

#=================================
# Bài 10: Xác suất ít nhất 1 lần trúng khi tung 3 con xúc xắc n lần:
n = int(input("Nhập n: "))
xac_suat_1_lan_trung = (1/6)**3
xac_suat_truot_het = (1 - xac_suat_1_lan_trung)**n
p = 1 - xac_suat_truot_het
print(f"Xác suất ít nhất 1 lần trúng: {p:.4f}")

#=================================
# Bài 11: Tính thời gian dừng:
import math
v_a = float(input("Nhập vận tốc a: "))
# Công thức: t = a^4 / log_4(5)
thoi_gian = (v_a**4) / math.log(5, 4)
print(f"Thời gian dừng: {thoi_gian:.2f} giây")