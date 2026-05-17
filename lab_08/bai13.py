def nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False
def so_ngay(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if nam_nhuan(nam):
            return 29
        return 28
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
print("Số ngày:", so_ngay(thang, nam))