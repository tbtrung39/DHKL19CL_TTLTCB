kw = float(input("Nhập số KW điện tiêu thụ: "))
if kw <= 100:
    tien = kw * 2000
elif kw <= 200:
    tien = 100 * 2000 + (kw - 100) * 2500
elif kw <= 300:
    tien = 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
else:
    tien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000
print(f"Tiền điện phải trả: {tien:,.0f} đồng")