gio = int(input("Nhập số giờ thuê: "))
gio_batdau = int(input("Nhập giờ bắt đầu: "))

if gio <= 3:
    tien = gio * 100000
else:
    tien = 3*100000 + (gio-3)*75000

if 11 <= gio_batdau <= 15:
    tien = tien * 0.9

print("Tiền thuê sân:", tien)