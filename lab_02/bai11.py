gio_bat_dau = int(input("Nhap gio bat dau: "))
gio_ket_thuc = int(input("Nhap gio ket thuc: "))
don_gia_moi_gio = float(input("Nhap don gia moi gio (dong): "))

if not (5 <= gio_bat_dau <= gio_ket_thuc <= 22):
    print("Du lieu khong hop le (yeu cau: 5 <= gio bat dau <= gio ket thuc <= 22).")
else:
    so_gio = gio_ket_thuc - gio_bat_dau
    tong_tien = so_gio * don_gia_moi_gio
    print("So tien khach phai tra:", int(tong_tien), "dong")