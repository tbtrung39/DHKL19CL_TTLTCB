def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        else:
            return 28

def kiem_tra_ngay(ngay, thang, nam):
    if thang < 1 or thang > 12:
        raise Exception("Thang khong hop le")
    if ngay < 1 or ngay > so_ngay_trong_thang(thang, nam):
        raise Exception("Ngay khong hop le")

def tinh_tong_ngay(ngay, thang, nam):
    tong = 0
    for y in range(1, nam):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            tong = tong + 366
        else:
            tong = tong + 365

    for t in range(1, thang):
        tong = tong + so_ngay_trong_thang(t, nam)
    tong = tong + ngay
    return tong

try:
    ngay1_str = input("Nhap ngay thu nhat (dd-mm-yyyy): ")
    ngay2_str = input("Nhap ngay thu hai (dd-mm-yyyy): ")

    phan1 = ngay1_str.split("-")
    phan2 = ngay2_str.split("-")

    if len(phan1) != 3 or len(phan2) != 3:
        raise Exception("Dinh dang ngay phai la dd-mm-yyyy!")

    ngay1, thang1, nam1 = int(phan1[0]), int(phan1[1]), int(phan1[2])
    ngay2, thang2, nam2 = int(phan2[0]), int(phan2[1]), int(phan2[2])

    kiem_tra_ngay(ngay1, thang1, nam1)
    kiem_tra_ngay(ngay2, thang2, nam2)

    tong1 = tinh_tong_ngay(ngay1, thang1, nam1)
    tong2 = tinh_tong_ngay(ngay2, thang2, nam2)

    khoang_cach = tong1 - tong2
    if khoang_cach < 0:
        khoang_cach = -khoang_cach

    nam_cach = khoang_cach // 365
    con_lai = khoang_cach % 365
    thang_cach = con_lai // 30
    ngay_cach = con_lai % 30

    print(f"Ngay 1: {ngay1_str}")
    print(f"Ngay 2: {ngay2_str}")
    print(f"Khoang cach: {khoang_cach} ngay")
    print(f"Tuong duong: {nam_cach} nam, {thang_cach} thang, {ngay_cach} ngay")

except ValueError:
    print("Loi: Vui long nhap so nguyen!")

except Exception as e:
    print(f"Loi: {e}")