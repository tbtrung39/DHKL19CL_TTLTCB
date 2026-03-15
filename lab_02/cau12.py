so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
if not (1 <= thang <= 12) or not (1 <= ngay <= so_ngay_trong_thang[thang - 1]):
    print("Ngày/tháng không hợp lệ!")
else:
    if ngay < so_ngay_trong_thang[thang - 1]:
        ngay_tiep = ngay + 1
        thang_tiep = thang
    elif thang < 12:
        ngay_tiep = 1
        thang_tiep = thang + 1
    else:
        ngay_tiep = 1
        thang_tiep = 1
    print(f"Ngày tiếp theo của {ngay}/{thang} là: {ngay_tiep}/{thang_tiep}")