import qlyhanghoa
# a. Nhập thông tin
danh_sach = qlyhanghoa.nhap_danh_sach_hang()

# b & c. Tính toán
qlyhanghoa.tinh_thanh_tien(danh_sach)
qlyhanghoa.tinh_thue(danh_sach)

# Hiện trạng trước khi sắp xếp
qlyhanghoa.hien_thi(danh_sach, "DANH SÁCH BAN ĐẦU")

# e. Sắp xếp giảm dần theo Thuế và hiển thị
ds_sap_xep = qlyhanghoa.sap_xep_giam_thue(danh_sach)
qlyhanghoa.hien_thi(ds_sap_xep, "DANH SÁCH GIẢM DẦN THEO THUẾ VAT")
