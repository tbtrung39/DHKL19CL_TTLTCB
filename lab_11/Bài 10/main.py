# Bài 10:
import csv
import os
from My_QuanLySinhvien import quanlysinhvien as ql

# 1. Nhập danh sách
danh_sach = ql.nhap_danh_sach()

# 2. Sắp xếp theo điểm RL tăng dần
danh_sach.sort(key=lambda x: x['RL'])

# 3. In thông tin sinh viên có điểm TL cao nhất
sv_top = max(danh_sach, key=lambda x: x['TL'])
print(f"\nSinh viên có điểm TL cao nhất là: {sv_top['Ten']} với {sv_top['TL']:.2f}")

# 4. Lưu vào file CSV
if not os.path.exists('files'): os.makedirs('files')
with open('files/ds_sinhvien.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["MSV", "Ten", "TB", "RL", "TL"])
    writer.writeheader()
    writer.writerows(danh_sach)

# 5. In bảng kết quả
ql.in_danh_sach(danh_sach)