#Bài 8:
import csv
import os
from libs import xu_ly_thong_tin_nhanvien as xu_ly

def main():
    ds_nv = []
    file_path = "files/ds_nhanvien.csv"

    while True:
        print("\n--- MENU ---")
        print("1. Nhập nhân viên | 2. Tính lương | 3. In bảng | 4. Sắp xếp | 5. Lưu file | 0. Thoát")
        choice = input("Chọn: ")

        if choice == '1':
            ma = input("Mã NV: ")
            ten = input("Tên NV: ")
            cv = input("Chức vụ (TP/PP/NV): ")
            hs = float(input("Hệ số lương: "))
            ds_nv.append({"Ma": ma, "Ten": ten, "ChucVu": cv, "HeSo": hs})
        
        elif choice == '2':
            for nv in ds_nv:
                l, pc, tl = xu_ly.tinh_luong(nv["HeSo"], nv["ChucVu"])
                nv.update({"Luong": l, "PhuCap": pc, "ThucLinh": tl})
            print("Đã tính xong lương.")

        elif choice == '3':
            print(f"{'Mã':<10} {'Tên':<15} {'Thực Lĩnh':<15}")
            for nv in ds_nv:
                print(f"{nv.get('Ma', 'N/A'):<10} {nv.get('Ten', 'N/A'):<15} {nv.get('ThucLinh', 0):<15}")

        elif choice == '4':
            ds_nv.sort(key=lambda x: x.get('ThucLinh', 0), reverse=True)
            print("Đã sắp xếp giảm dần theo Thực lĩnh.")

        elif choice == '5':
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["Ma", "Ten", "ChucVu", "HeSo", "Luong", "PhuCap", "ThucLinh"])
                writer.writeheader()
                writer.writerows(ds_nv)
            print("Đã lưu vào files/ds_nhanvien.csv")
            
        elif choice == '0': break

if __name__ == "__main__":
    # Đảm bảo thư mục files tồn tại
    if not os.path.exists('files'): os.makedirs('files')
    main()