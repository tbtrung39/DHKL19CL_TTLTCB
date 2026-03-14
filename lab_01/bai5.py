t = float(input("Nhap thoi gian su dung (giay): "))
U = 220
I = 2.7
P = U * I
dien_nang = (P * t) / 3600000
tien_dien = dien_nang * 7000
print(f"So tien phai tra la: {tien_dien}")