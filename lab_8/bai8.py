import math

def tinh_hinh_tron(ban_kinh):
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * (ban_kinh ** 2)
    return chu_vi, dien_tich

r = float(input("Nhập bán kính hình tròn: "))
cv, dt = tinh_hinh_tron(r)
print(f"Chu vi: {cv:.2f}")
print(f"Diện tích: {dt:.2f}")