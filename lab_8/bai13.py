def kiem_tra_nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def so_ngay_trong_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if kiem_tra_nam_nhuan(y) else 28
    return 0 
year = int(input("Nhập năm: "))
month = int(input("Nhập tháng: "))

print(f"Năm {year} có phải năm nhuận không? {kiem_tra_nam_nhuan(year)}")
print(f"Tháng {month}/{year} có tối đa: {so_ngay_trong_thang(month, year)} ngày.")