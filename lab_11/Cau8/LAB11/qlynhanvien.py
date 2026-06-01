from libs.xu_ly_thong_tin_nhanvien import *
ds = []
while True:
    print("1. Nhap danh sach nhan vien")
    print("2. Hien thi danh sach ")
    print("3. Sap xep  theo thuc linh giam dan")
    print("4. Luu  vao file")
    print("0. Thoat")
    chon = int(input("Nhap lua chon: "))
    if chon == 1:
        ds = nhap_danh_sach()
    elif chon == 2:
        hien_thi(ds)
    elif chon == 3:
        sap_xep(ds)
        print("Da sap xep.")
        hien_thi(ds)
    elif chon == 4:
        luu_file(ds,"files/ds_nhanvien.csv")
        print("Da luu vao file.")
    elif chon == 0:
        print("Thoat chuong trinh.")
        break
    else:
        print("Lua chon khong hop le!")