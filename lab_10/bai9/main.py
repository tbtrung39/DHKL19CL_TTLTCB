import qlyhanghoa

# a. Nhap danh sach
danh_sach = qlyhanghoa.nhap_danh_sach_hang()

# b & c. Tinh toan
qlyhanghoa.tinh_thanh_tien_va_vat(danh_sach)

# e. In ra truoc khi sap xep
qlyhanghoa.in_danh_sach(danh_sach, "DANH SÁCH BAN ĐẦU")

# e. Sap xep va in ra sau khi sap xep
ds_sap_xep = qlyhanghoa.sap_xep_giam_dan_theo_thue(danh_sach)
qlyhanghoa.in_danh_sach(ds_sap_xep, "DANH SÁCH GIẢM DẦN THEO THUẾ VAT")