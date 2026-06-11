from quanlysinhvien import (
    nhap_danh_sach_sv,
    tinh_diem_tl,
    in_va_luu_danh_sach,
    sap_xep_tang_dan_diem_rl,
    in_sinh_vien_max_diem_tl
)

def menu():
    print("\n--- QUẢN LÝ SINH VIÊN ---")
    print("1. Nhập danh sách sinh viên")
    print("2. Tính điểm tích lũy (TL)")
    print("3. In danh sách dạng bảng & Lưu vào ds_sinhvien.csv")
    print("4. Sắp xếp danh sách tăng dần theo điểm rèn luyện (RL)")
    print("5. In thông tin sinh viên có điểm TL cao nhất")
    print("0. Thoát")
    return input("Chọn chức năng (0-5): ")

def main():
    danh_sach = []
    while True:
        user_choice = menu()
        if user_choice == '1':
            danh_sach = nhap_danh_sach_sv()
        elif user_choice == '2':
            if danh_sach:
                danh_sach = tinh_diem_tl(danh_sach)
                print("-> Đã tính xong điểm tích lũy.")
            else:
                print("Vui lòng nhập danh sách sinh viên trước.")
        elif user_choice == '3':
            if danh_sach:
                in_va_luu_danh_sach(danh_sach)
            else:
                print("Danh sách rỗng.")
        elif user_choice == '4':
            if danh_sach:
                ds_sap_xep = sap_xep_tang_dan_diem_rl(danh_sach)
                print("\nDanh sách sau khi sắp xếp tăng dần theo Điểm RL:")
                for sv in ds_sap_xep:
                    print(f"Mã SV: {sv['ma_sv']} | Tên: {sv['ho_ten']} | Điểm RL: {sv['diem_rl']}")
            else:
                print("Danh sách rỗng.")
        elif user_choice == '5':
            if danh_sach:
                in_sinh_vien_max_diem_tl(danh_sach)
            else:
                print("Danh sách rỗng.")
        elif user_choice == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == '__main__':
    pass 