ngay = int(input("Nhap ngay: "))
thang = int(input("Nhap thang: "))
ngay_trong_thang = [31,28,31,30,31,30,31,31,30,31,30,31]
if ngay < ngay_trong_thang[thang - 1]:
    ngay = ngay + 1
else:
    ngay = 1
    if thang == 12:
        thang = 1
    else:
        thang = thang + 1
print("Ngay tiep theo: ", ngay, "/", thang)
