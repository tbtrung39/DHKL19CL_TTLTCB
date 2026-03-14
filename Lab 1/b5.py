U = 220
I = 2.7
gia_tien = 7000
t = float(input("Nhập thời gian sử dụng (giây): "))
công_suất = U * I
năng_lượng_joule = công_suất * t
so_kwh = năng_lượng_joule / 3600000
tien_dien = so_kwh * gia_tien
print(f"Tiền điện phải trả là: {round(tien_dien, 2)}đ")