#nhập số thập phân
so_thap_phan = float(input("Nhập một số thập phân: "))

so_nguyen = int(so_thap_phan)
print(so_nguyen)

chuoi = ""

if so_nguyen == 0:
    chuoi = "khong"

while so_nguyen > 0:
    du = so_nguyen % 10

    if du == 0:
        chuoi = "khong " + chuoi
    elif du == 1:
        chuoi = "mot " + chuoi
    elif du == 2:
        chuoi = "hai " + chuoi
    elif du == 3:
        chuoi = "ba " + chuoi
    elif du == 4:
        chuoi = "bon " + chuoi
    elif du == 5:
        chuoi = "nam " + chuoi
    elif du == 6:
        chuoi = "sau " + chuoi
    elif du == 7:
        chuoi = "bay " + chuoi
    elif du == 8:
        chuoi = "tam " + chuoi
    elif du == 9:
        chuoi = "chin " + chuoi
    so_nguyen //= 10

print(chuoi)