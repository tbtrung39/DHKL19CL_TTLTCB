#bài2
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        print("Vô số nghiệm" if c == 0 else "Vô nghiệm")
    else:
        print(f"Nghệm x = {-c/b}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print(f"Nghệm kép x = {-b/(2*a)}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"x1 = {x1}, x2 = {x2}")
#bài4
n = int(input("Nhập số nguyên: "))
hang_tram = (abs(n) // 100) % 10
print(f"Chữ số hàng trăm: {hang_tram}")
#bài6
n = int(input("Nhập số có 3 chữ số: "))
if 100 <= n <= 999:
    dv = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tram = n // 100
    chuc = (n // 10) % 10
    don_vi = n % 10
    print(f"Cách đọc: {dv[tram]} trăm {dv[chuc]} mươi {dv[don_vi]}")
else:
    print("Không phải số có 3 chữ số.")
#bài8
tnct = float(input("Nhập thâm niên công tác (tháng): "))
luong_cb = 1350000

if tnct < 12: he_so = 2.34
elif tnct < 36: he_so = 3.33
elif tnct < 60: he_so = 3.66
else: he_so = 3.99

luong = he_so * luong_cb
print(f"Lương của nhân viên: {luong:,.0f} đồng")
#bài10
gio_thue = float(input("Nhập số giờ thuê: "))
bat_dau = int(input("Nhập giờ bắt đầu (0-23): "))

# Tính tiền theo giờ
if gio_thue <= 3:
    tong_tien = gio_thue * 100000
else:
    tong_tien = (3 * 100000) + (gio_thue - 3) * 100000 * 0.75

# Giảm giá khung giờ vàng (11h-15h)
if 11 <= bat_dau <= 15:
    tong_tien *= 0.9

print(f"Số tiền phải trả: {tong_tien:,.0f} đồng")
#bai12
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
# Số ngày trong tháng của năm không nhuận
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= m <= 12 and 1 <= d <= days[m]:
    d += 1
    if d > days[m]:
        d = 1
        m += 1
        if m > 12:
            m = 1
    print(f"Ngày tiếp theo là: {d}/{m}")
else:
    print("Ngày tháng không hợp lệ!")
