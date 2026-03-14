def tinh_tien(bat_dau, ket_thuc):
    so_gio = ket_thuc - bat_dau
    if so_gio <= 3:
        tien = so_gio * 100000
    else:
        tien = 3*100000 + (so_gio - 3) * 75000
    if bat_dau >= 11 and ket_thuc <= 15:
        tien = tien * 0.9
    return tien
