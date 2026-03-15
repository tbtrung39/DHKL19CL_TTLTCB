#chuong2
# 1
def ngay_trong_thang():
    m = int(input("Nhập tháng: "))
    if m in [1,3,5,7,8,10,12]:
        print("31 ngày")
    elif m in [4,6,9,11]:
        print("30 ngày")
    elif m == 2:
        print("28 hoặc 29 ngày")
    else:
        print("Tháng không hợp lệ")


# 2
def giai_pt_bac_hai():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a == 0:
        if b == 0:
            if c == 0:
                print("Vô số nghiệm")
            else:
                print("Vô nghiệm")
        else:
            x = -c/b
            print("Nghiệm:", x)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("Vô nghiệm")
        elif delta == 0:
            x = -b/(2*a)
            print("Nghiệm kép:", x)
        else:
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (-b - delta**0.5)/(2*a)
            print("x1 =", x1, "x2 =", x2)


# 3
def thu_trong_tuan():
    while True:
        n = int(input("Nhập thứ (1-7): "))
        if 1 <= n <= 7:
            break

    ds_thu = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    print(ds_thu[n-1])


# 4
def chu_so_hang_tram():
    n = int(input("Nhập số nguyên: "))
    print((abs(n)//100) % 10)


# 5
def ten_thang():
    while True:
        m = int(input("Nhập tháng (1-12): "))
        if 1 <= m <= 12:
            break

    ds_thang = ["January","February","March","April","May","June",
                "July","August","September","October","November","December"]

    print(ds_thang[m-1])


# 6
def doc_so_ba_chu_so():
    n = int(input("Nhập số có 3 chữ số: "))
    tram = n // 100
    chuc = (n % 100) // 10
    donvi = n % 10

    print(tram, "trăm", chuc, "mươi", donvi)


# 7
def xep_loai_hoc_luc():
    x = float(input("Nhập điểm TK: "))

    if x < 3:
        print("Loại Kém")
    elif x < 5:
        print("Loại Yếu")
    elif x < 7:
        print("Loại Trung bình")
    elif x < 8:
        print("Loại Khá")
    elif x < 9:
        print("Loại Giỏi")
    else:
        print("Loại Xuất sắc")


# 8
def tinh_luong_nhan_vien():
    tnct = int(input("Nhập thâm niên công tác (tháng): "))
    luong_co_ban = 1350000

    if tnct < 12:
        he_so = 2.34
    elif tnct < 36:
        he_so = 3.33
    elif tnct < 60:
        he_so = 3.66
    else:
        he_so = 3.99

    luong = he_so * luong_co_ban
    print("Lương:", luong)


# 9
def tinh_tien_dien():
    kw = int(input("Nhập số KW: "))

    if kw <= 100:
        don_gia = 2000
    elif kw <= 200:
        don_gia = 2500
    elif kw <= 300:
        don_gia = 3000
    else:
        don_gia = 5000

    tien = kw * don_gia
    print("Tiền điện:", tien)


# 10
def tien_thue_san():
    gio = int(input("Nhập số giờ thuê: "))

    if gio <= 3:
        tien = gio * 100000
    else:
        tien = 3*100000 + (gio-3)*75000

    print("Tiền thuê:", tien)


# 11
def tien_thue_san_day_du():
    bat_dau = int(input("Giờ bắt đầu: "))
    ket_thuc = int(input("Giờ kết thúc: "))

    so_gio = ket_thuc - bat_dau

    if so_gio <= 3:
        tien = so_gio * 100000
    else:
        tien = 3*100000 + (so_gio-3)*75000

    if 11 <= bat_dau <= 15:
        tien *= 0.9

    print("Tiền phải trả:", tien)


# 12
def ngay_tiep_theo():
    d = int(input("Ngày: "))
    m = int(input("Tháng: "))
    y = int(input("Năm: "))

    ds_ngay = [31,28,31,30,31,30,31,31,30,31,30,31]

    d += 1
    if d > ds_ngay[m-1]:
        d = 1
        m += 1

    if m > 12:
        m = 1
        y += 1

    print("Ngày tiếp theo:", d, "/", m, "/", y)


ngay_trong_thang()
giai_pt_bac_hai()
tinh_tien_dien()
thu_trong_tuan()
chu_so_hang_tram()
ten_thang()
doc_so_ba_chu_so()
xep_loai_hoc_luc()
tinh_luong_nhan_vien()
tien_thue_san()
tien_thue_san_day_du()
ngay_tiep_theo()

