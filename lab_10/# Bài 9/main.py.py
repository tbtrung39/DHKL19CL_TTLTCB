# bài 9:
import qlyhanghoa

# 1. Nhập số lượng hàng hóa
n = int(input("Nhập số lượng mặt hàng cần quản lý: "))

# 2. Nhập thông tin
danh_sach = qlyhanghoa.nhap_danh_sach_hang_hoa(n)

# 3. Hiển thị trước khi sắp xếp
print("\n--- DANH SÁCH BAN ĐẦU ---")
qlyhanghoa.hien_thi(danh_sach)

# 4. Sắp xếp và hiển thị sau khi sắp xếp
qlyhanghoa.sap_xep_giam_dan_theo_thue(danh_sach)
print("\n--- DANH SÁCH SAU KHI SẮP XẾP THEO THUẾ GIẢM DẦN ---")
qlyhanghoa.hien_thi(danh_sach)