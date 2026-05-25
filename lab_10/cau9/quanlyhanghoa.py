def nhap_hang():
    ma = input("Nhap ma hang: ")
    ten = input("Nhap ten hang: ")
    dvt = input("Nhap don vi tinh: ")
    dongia = input("Nhap don gia: ")
    dongia = float(dongia)
    soluong = input("Nhap so luong: ")
    soluong = int(soluong)
    thanhtien = dongia * soluong
    thue = thanhtien * 0.1
    return [ma, ten, dvt, dongia, soluong, thanhtien, thue]
def xuat(ds):
    for x in ds:
        print(x)
def sap_xep(ds):
    n = len(ds)
    for i in range(n):
        for j in range(i + 1, n):
            if ds[i][6] < ds[j][6]:
                t = ds[i]
                ds[i] = ds[j]
                ds[j] = t
