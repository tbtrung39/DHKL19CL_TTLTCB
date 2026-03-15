U = 220
I = 2.7
don_gia = 7000

t_giay = float(input("Nhập thời gian sử dụng (giây): "))

t_gio = t_giay / 3600

kwh = (U * I * t_gio) / 1000

tong_tien = kwh * don_gia
print(f"Số tiền điện phải trả là: {round(tong_tien, 2)} VNĐ")