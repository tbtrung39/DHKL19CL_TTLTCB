try:
    ngay1 = input("Nhap ngay thu nhat (dd-mm-yyyy): ")
    ngay2 = input("Nhap ngay thu hai (dd-mm-yyyy): ")
    d1, m1, y1 = map(int, ngay1.split("-"))
    d2, m2, y2 = map(int, ngay2.split("-"))
    if (y1, m1, d1) > (y2, m2, d2):
        d1,d2 = d2,d1
        m1,m2 = m2,m1
        y1,y2 = y2,y1
    def sngay_trong_thang(m, y):
        if m in [1,3,5,7,8,10,12]:
            return 31
        elif m in [4,6,9,11]:
            return 30
        else:
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                return 29
            else:
                return 28
    nam = y2 - y1
    thang = m2 - m1
    ngay = d2 - d1
    if ngay < 0:
        thang = thang - 1
        thang_truoc = m2 - 1
        if thang_truoc == 0:
            thang_truoc = 12
            nam_truoc = y2 - 1
        else:
            nam_truoc = y2
        ngay = ngay + sngay_trong_thang(thang_truoc, nam_truoc)
    if thang < 0:
        nam = nam - 1
        thang = thang + 12
    print("Khoang cach giua hai ngay la: ", nam, "nam", thang, "thang", ngay, "ngay")
except ValueError:
    print("Dinh dang ngay khong hop le!")
except Exception as e:
    print(e)