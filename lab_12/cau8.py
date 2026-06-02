try:
    ngay = input("Nhap ngay: ")
    ngay = int(ngay)
    thang = input("Nhap thang: ")
    thang = int(thang)
    nam = input("Nhap nam: ")
    nam = int(nam)
    if thang < 1 or thang > 12:
        raise Exception("Thang khong hop le!")
    if thang in [1,3,5,7,8,10,12]:
        so_ngay = 31
    elif thang in [4,6,9,11]:
        so_ngay = 30
    else:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            so_ngay = 29
        else:
            so_ngay = 28
    if ngay < 1 or ngay > so_ngay:
        raise Exception("Ngay khong hop le!")
    ngay = ngay - 1
    if ngay == 0:
        thang = thang - 1
        if thang == 0:
            thang = 12
            nam = nam - 1
        if thang in [1,3,5,7,8,10,12]:
            ngay = 31
        elif thang in [4,6,9,11]:
            ngay = 30
        else:
            if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
                ngay = 29
            else:
                ngay = 28
    print("Ngay truoc do la: ", ngay, "/", thang, "/", nam)
except Exception as e:
    print(e)