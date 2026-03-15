# Bài 2
import math
a, b, c = map(float, input("Nhập a b c: ").split())
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print(f"Phương trình bậc 1 có nghiệm x = {x:.2f}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")

# Bài 4
n = input("Nhập số nguyên: ")
num = int(n)
if num >= 100 or num <= -100:
    hang_trăm = abs(num) // 100 % 10
    print("Chữ số hàng trăm là:", hang_trăm)
else:
    print("0")

# Bài 6
n = input("Nhập số nguyên có 3 chữ số: ")
num = int(n)
tram = num // 100
chuc = (num % 100) // 10
don_vi = num % 10
print(f"{tram} trăm {chuc} chục {don_vi} đơn vị")

# Bài 8
n = input("Nhập thâm niên (tháng): ")
nl = int(n)
luong_cb = 1350000
if nl < 12:
    print("Lương của bạn là: ", luong_cb)
elif nl >= 12 and nl < 36:
    print("Lương của bạn là: ", luong_cb * 1.1)
elif nl >= 36 and nl < 60:
    print("Lương của bạn là: ", luong_cb * 1.2)
elif nl >= 60 and nl < 120:
    print("Lương của bạn là: ", luong_cb * 1.3)
else:
    print("Lương của bạn là: ", luong_cb * 1.5)

# Bài 10
def tinh_tien(Start, End):
    so_gio = End - Start
    if so_gio <= 3:
        tien = so_gio * 100000
    else:
        tien = 3*100000 + (so_gio - 3) * 75000
    if Start >= 11 and End <= 15:
        tien = tien * 0.9
    return tien

bat_dau = int(input("Nhập giờ bắt đầu: "))
ket_thuc = int(input("Nhập giờ kết thúc: "))
if 5 <= bat_dau <= ket_thuc <= 22:
    tien = tinh_tien(bat_dau, ket_thuc)
    print(f"Số tiền cần trả là: {tien} đồng")
else:
    print("Thời gian không hợp lệ.")
