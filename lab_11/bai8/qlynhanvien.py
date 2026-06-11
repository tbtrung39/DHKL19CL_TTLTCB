import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'libs'))
from xu_ly_thong_tin import tinh_luong_va_phu_cap, luu_file_csv

def hien_thi_menu():
    print("\n========= MENU QUẢN LÝ NHÂN VIÊN =========")
    print("a. Nhập danh sách nhân viên từ bàn phím")
    print("b. Tính Lương, Phụ cấp và Thực lĩnh")
    print("c. In danh sách nhân viên dạng bảng")
    print("d. Sắp xếp danh sách giảm dần theo Thực lĩnh & in ra")
    print("e. Lưu dữ liệu vào file ds_nhanvien.csv")
    print("q. Thoát chương trình")
    return input("Chọn chức năng (a/b/c/d/e/q): ").strip().lower()

def nhap_nhan_vien():
    ds = []
    n = int(input("Nhập số lượng nhân viên cần thêm: "))
    for i in range(n):
        print(f"\n--- Nhập thông tin nhân viên thứ {i+1} ---")
        ma_nv = input("Mã NV: ")
        ten_nv = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        he_so = float(input("Hệ số lương: "))
        
        nv = {
            'Ma_NV': ma_nv,
            'Ten_NV': ten_nv,
            'Chuc_vu': chuc_vu,
            'He_so_luong': he_so,
            'Luong': 0,
            'Phu_cap': 0,
            'Thuc_linh': 0
        }
        ds.append(nv)
    return ds

def in_dang_bang(ds):
    print(f"{'Mã NV':<10}{'Tên NV':<20}{'Chức vụ':<10}{'Hệ số':<10}{'Lương':<15}{'Phụ cấp':<12}{'Thực lĩnh':<15}")
    print("-" * 92)
    for nv in ds:
        print(f"{nv['Ma_NV']:<10}{nv['Ten_NV']:<20}{nv['Chuc_vu']:<10}{nv['He_so_luong']:<10}{nv['Luong']:<15,.0f}{nv['Phu_cap']:<12,.0f}{nv['Thuc_linh']:<15,.0f}")

def main():
    danh_sach_nv = []
    csv_path = os.path.join(os.path.dirname(__file__), 'files', 'ds_nhanvien.csv')
    
    while True:
        choice = hien_thi_menu()
        if choice == 'a':
            danh_sach_nv.extend(nhap_nhan_vien())
            print("-> Đã nhập danh sách thành công.")
        elif choice == 'b':
            if not danh_sach_nv:
                print("Chưa có dữ liệu nhân viên. Hãy nhập trước (chức năng a).")
            else:
                danh_sach_nv = [tinh_luong_va_phu_cap(nv) for nv in danh_sach_nv]
                print("-> Đã tính toán xong Lương, Phụ cấp, Thực lĩnh.")
        elif choice == 'c':
            if not danh_sach_nv:
                print("Danh sách trống.")
            else:
                print("\nDANH SÁCH NHÂN VIÊN HIỆN TẠI:")
                in_dang_bang(danh_sach_nv)
        elif choice == 'd':
            if not danh_sach_nv:
                print("Danh sách trống.")
            else:
                ds_sap_xep = sorted(danh_sach_nv, key=lambda x: x['Thuc_linh'], reverse=True)
                print("\nDANH SÁCH SẮP XẾP GIẢM DẦN THEO THỰC LĨNH:")