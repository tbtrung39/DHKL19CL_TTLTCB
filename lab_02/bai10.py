thoi_gian_thue_dau = int(input("Ban thue san bat dau tu may gio: "))
thoi_gian_thue_ket_thuc = int(input("Ban thue san ket thuc vao may gio: "))

GIA_3_GIO_DAU = 100000          # 100,000d/gio
GIA_GIO_TIEP  = GIA_3_GIO_DAU * 0.75  # giam 25%

if not (0 <= thoi_gian_thue_dau <= 24) or not (0 <= thoi_gian_thue_ket_thuc <= 24):
    print("Thoi gian thue phai nam trong khoang 0-24 gio!")
elif thoi_gian_thue_ket_thuc <= thoi_gian_thue_dau:
    print("Thoi gian ket thuc phai lon hon thoi gian bat dau!")
else:
    so_gio = thoi_gian_thue_ket_thuc - thoi_gian_thue_dau

    # Tinh tien theo so gio thue
    if so_gio <= 3:
        tong_tien = so_gio * GIA_3_GIO_DAU
    else:
        tong_tien = 3 * GIA_3_GIO_DAU + (so_gio - 3) * GIA_GIO_TIEP

    # Giam them 10% neu thue trong khung 11-15 gio
    if thoi_gian_thue_dau >= 11 and thoi_gian_thue_ket_thuc <= 15:
        tong_tien = tong_tien * 0.9

    print("So gio thue:", so_gio, "gio")
    print("Tong tien thue san:", int(tong_tien), "dong")
