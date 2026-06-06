import csv, os, sys
sys.path.append(r"bai8\libs")
from xu_ly_thong_tin_nhanvien import *

os.makedirs("files", exist_ok=True)
ds = []

while True:
    print("1. Nhập danh sách nhân viên")
    print("2. Tính lương và hiển thị bảng")
    print("3. Sắp xếp theo thực lĩnh giảm dần")
    print("4. Lưu ra file CSV")
    print("0. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        n = int(input("Số nhân viên: "))
        for i in range(n):
            print(f"\n-- Nhân viên {i+1} --")
            ds.append(nhap_nhan_vien())

    elif chon == "2":
        if ds:
            in_bang(ds)
        else:
            print("Chưa có dữ liệu!")

    elif chon == "3":
        ds.sort(key=lambda x: x["thuc_linh"], reverse=True)
        print("Danh sách sau sắp xếp:")
        in_bang(ds)

    elif chon == "4":
        with open("files/ds_nhanvien.csv", "w", newline="", encoding="utf-8-sig") as f:
            fieldnames=["ma","ten","chuc_vu","he_so","luong","phu_cap","thuc_linh"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(ds)
        print("Đã lưu vào files/ds_nhanvien.csv!")

    elif chon == "0":
        break