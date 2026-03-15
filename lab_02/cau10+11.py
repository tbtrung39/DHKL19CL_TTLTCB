bat_dau = int(input('nhap gio bat dau(5-22h): '))
ket_thuc = int(input('nhap gio ket thuc(5-22h): '))
if not  5<=bat_dau <= ket_thuc<=22 :
    print('gio khong hop le')
else:
    so_gio = ket_thuc - bat_dau
    don_gia_dau = 100000
    don_gia_sau = 100000*0.75
    if so_gio <= 3:
        tien = so_gio *don_gia_dau
    else:
        tien = 3*don_gia_dau + (so_gio-3)*don_gia_sau
    if bat_dau >=11 and ket_thuc<=15:
        tien = tien * 0.9
    print('so tien phai tra: ',tien,'dong')