#câu1
thang = int(input("Nhap thang: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print("Thang co 31 ngay")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print("Thang co 30 ngay")
elif thang == 2:
    print("Thang co 28 ngay")
else:
    print("Thang khong hop le")
#câu2
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x = -c / b
        print("Nghiem x =", x)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b/(2*a)
        print("Nghiem kep x =", x)
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        print("x1 =", x1)
        print("x2 =", x2)
#câu3
thu = int(input("Nhap thu (1-7): "))
if thu == 1:
    print("Sunday")
elif thu == 2:
    print("Monday")
elif thu == 3:
    print("Tuesday")
elif thu == 4:
    print("Wednesday")
elif thu == 5:
    print("Thursday")
elif thu == 6:
    print("Friday")
elif thu == 7:
    print("Saturday")
else:
    print("Thu khong hop le")
#câu4
n = int(input("Nhap so nguyen: "))
if n < 100:
    print("Chu so hang tram = 0")
else:
    tram = (n // 100) % 10
    print("Chu so hang tram =", tram)
#câu5
thang = int(input("Nhap thang (1-12): "))
if thang == 1:
    print("January")
elif thang == 2:
    print("February")
elif thang == 3:
    print("March")
elif thang == 4:
    print("April")
elif thang == 5:
    print("May")
elif thang == 6:
    print("June")
elif thang == 7:
    print("July")
elif thang == 8:
    print("August")
elif thang == 9:
    print("September")
elif thang == 10:
    print("October")
elif thang == 11:
    print("November")
elif thang == 12:
    print("December")
else:
    print("Thang khong hop le")
#câu6
n = int(input("Nhap so co 3 chu so: "))
tram = n // 100
chuc = (n // 10) % 10
donvi = n % 10
print("So vua nhap:", tram, chuc, donvi)
#câu7
diem = float(input("Nhap diem trung binh: "))
if diem <= 3:
    print("Loai Kem")
elif diem <= 4:
    print("Loai Yeu")
elif diem <= 6:
    print("Loai Trung Binh")
elif diem <= 8:
    print("Loai Kha")
elif diem <= 9:
    print("Loai Gioi")
elif diem <= 10:
    print("Loai Xuat Sac")
else:
    print("Diem khong hop le")
#câu8
tnct = int(input("Nhap tham nien cong tac (thang): "))
luong_cb = 1350000
if tnct < 12:
    he_so = 2.34
elif tnct <= 36:
    he_so = 3.33
elif tnct < 60:
    he_so = 3.66
else:
    he_so = 3.99
luong = he_so * luong_cb
print("Luong =", luong)
#câu9
kw = int(input("Nhap so KW dien: "))
if kw <= 100:
    tien = kw * 2000
elif kw <= 200:
    tien = kw * 2500
elif kw <= 300:
    tien = kw * 3000
else:
    tien = kw * 5000
print("Tien dien =", tien)
#câu10
gio = int(input("Nhap so gio thue san: "))

if gio <= 3:
    tien = gio * 100000
else:
    tien = 3 * 100000 + (gio - 3) * 75000

print("Tien thue san =", tien)
#câu11
gio_bat_dau = int(input("Nhap gio bat dau: "))
gio_ket_thuc = int(input("Nhap gio ket thuc: "))
gio = gio_ket_thuc - gio_bat_dau
if gio <= 3:
    tien = gio * 100000
else:
    tien = 3 * 100000 + (gio - 3) * 75000
if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
    tien = tien * 0.9
print("Tien phai tra =", tien)
#câu12
ngay = int(input("Nhap ngay: "))
thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10:
    if ngay < 31:
        ngay += 1
    else:
        ngay = 1
        thang += 1
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    if ngay < 30:
        ngay += 1
    else:
        ngay = 1
        thang += 1
elif thang == 2:
    if ngay < 28:
        ngay += 1
    else:
        ngay = 1
        thang = 3
elif thang == 12:
    if ngay < 31:
        ngay += 1
    else:
        ngay = 1
        thang = 1
        nam += 1
print("Ngay tiep theo:", ngay, "/", thang, "/", nam)