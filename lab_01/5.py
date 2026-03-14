t = float(input("Nhập thời gian sử dụng (giây): "))

U = 220
I = 2.7
P = U * I

dien = (P * t) / (1000 * 3600)

tien = dien * 7000

print("Số tiền điện:", round(tien,2))