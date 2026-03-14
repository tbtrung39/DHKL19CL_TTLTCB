gio = int(input("Nhap so gio thue: "))
gia = 100000
tong = 0
if gio <= 3:
    tong = gio * gia
else:
    tong = 3 * gia + (gio - 3) * (gia * 0.75)
print("Tien thue san = ", tong)