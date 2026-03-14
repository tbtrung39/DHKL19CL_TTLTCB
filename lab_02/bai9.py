so_dien = input("Nhập số điện tiêu thụ (KW): ")
so_dien_tt = int(so_dien)
if so_dien_tt <= 100:
    don_gia = 2000
elif 101 <= so_dien_tt <= 200:
    don_gia = 2500
elif 201 <= so_dien_tt <= 300:
    don_gia = 3000
elif so_dien_tt >300:
    don_gia = 5000
tien_dien = so_dien_tt * don_gia
print(f"Số tiền điện phải trả là: {tien_dien} VNĐ")
