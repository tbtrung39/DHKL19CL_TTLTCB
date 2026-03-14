from Bai10 import tinh_tien
bat_dau = int(input("Nhập giờ bắt đầu: "))
ket_thuc = int(input("Nhập giờ kết thúc: "))
if 5 <= bat_dau <= ket_thuc <= 22:
    tien = tinh_tien(bat_dau, ket_thuc)
    print(f"Số tiền cần trả là: {tien} đồng")
else:
    print("Thời gian không hợp lệ.")