def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        else:
            return 28

try:
    ngay = int(input("Nhap ngay: "))
    thang = int(input("Nhap thang: "))
    nam = int(input("Nhap nam: "))

    if nam < 1:
        raise Exception("Nam khong hop le")
    if thang < 1 or thang > 12:
        raise Exception("Thang khong hop le")
    if ngay < 1 or ngay > so_ngay_trong_thang(thang, nam):
        raise Exception("Ngay khong hop le")
    
    ngay_trc = ngay + 1
    thang_trc = thang
    nam_trc = nam

    if ngay_ke > so_ngay_trong_thang(thang, nam):
        ngay_ke = 1
        thang_ke = thang + 1

    if thang_ke > 12:
        thang_ke = 1
        nam_ke = nam + 1

    print(f"Ngay nhap vao : {ngay}/{thang}/{nam}")
    print(f"Ngay ke tiep  : {ngay_ke}/{thang_ke}/{nam_ke}")

except ValueError:
    print("Loi: Vui long nhap so nguyen")

except Exception as e:
    print(f"Loi: {e}")