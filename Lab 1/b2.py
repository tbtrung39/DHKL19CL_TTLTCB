print("--- Đổi thời gian ---")
d = int(input("Nhập số ngày (d): "))
h = int(input("Nhập số giờ (h): "))
m = int(input("Nhập số phút (m): "))
s = int(input("Nhập số giây (s): "))
tong_giay = d * 86400 + h * 3600 + m * 60 + s

print(f"Tổng số giây là: {tong_giay}")
print("\n--- Tính toán khối trụ ---")
pi = 3.14
r = float(input("Nhập bán kính r: "))
h_tru = float(input("Nhập chiều cao h: "))
s_xq = 2 * pi * r * h_tru
s_tp = s_xq + 2 * pi * (r**2)
the_tich = pi * (r**2) * h_tru
print(f"Diện tích xung quanh: {round(s_xq, 2)}")
print(f"Diện tích toàn phần: {round(s_tp, 2)}")
print(f"Thể tích khối trụ: {round(the_tich, 2)}")