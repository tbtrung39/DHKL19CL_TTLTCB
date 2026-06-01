from My_Quanlysinhvien.quanlysinhvien import *
ds = []
while True:
    print("1. Nhap danh sach")
    print("2. Hien thi danh sach")
    print("3. Sap xep theo diem RL tang dan")
    print("4. Tim sinh vien co diem TL cao nhat")
    print("5. Luu file")
    print("0. Thoat")
    chon = int(input("Nhap lua chon: "))
    if chon == 1:
        ds = nhap_danh_sach()
    elif chon == 2:
        hien_thi(ds)
    elif chon == 3:
        sap_xep(ds)
        print("\nDa sap xep!")
        hien_thi(ds)
    elif chon == 4:
        sv = tim_max_tl(ds)
        print("\nSINH VIEN CO DIEM TL CAO NHAT")
        print("Ma SV:", sv["MaSV"])
        print("Ho ten:", sv["HoTen"])
        print("TB:", sv["TB"])
        print("RL:", sv["RL"])
        print("TL:", sv["TL"])
    elif chon == 5:
        luu_file(ds, "files/ds_sinhvien.csv")
    elif chon == 0:
        print("Ket thuc chuong trinh")
        break
    else:
        print("Lua chon khong hop le!")