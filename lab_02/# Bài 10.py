# Bài 10:
def tinh_tien(Start, End):
    so_gio = End - Start
    if so_gio <= 3:
        tien = so_gio * 100000
    else:
        tien = 3*100000 + (so_gio - 3) * 75000
    if Start >= 11 and End <= 15:
        tien = tien * 0.9
    return tien

# Bai 11:
from Bai10 import tinh_tien
bat_dau = int(input("Nhập giờ bắt đầu: "))
ket_thuc = int(input("Nhập giờ kết thúc: "))
if 5 <= bat_dau <= ket_thuc <= 22:
    tien = tinh_tien(bat_dau, ket_thuc)
    print(f"Số tiền cần trả là: {tien} đồng")
else:
    print("Thời gian không hợp lệ.")