#cau1
def value(x):
    print(x + 1)
n = input("Nhap so n:")
n = int(n)
value(n)
#cau2
a = input("Nhap vao a: ")
a = int(a)
b = input("Nhap vao b: ")
b = int(b)
def UCLN(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
t = UCLN(a, b)
def value(a,b,t):
    a = a / t
    b = b / t
    print(f'phan so rut gon la:{int(a)}/{int(b)}')
value(a,b,t)
#cau3
def kt_nguyento(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
n = input("Nhap vao n: ")
n = int(n)
for i in range(1,n):
    if kt_nguyento(i):
        print(i, end=' ')
#cau4
n = input("Nhap mot so nguyen n: ")
n = int(n)
def lap_phuong(x):
    print(x**3)
lap_phuong(n)
#cau5
a = input("Nhap vao a: ")
a = int(a)
b = input("Nhap vao b: ")
b = int(b)
def UCLN(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
print(UCLN(a, b))
#cau6
a = input("Nhap vao a: ")
a = int(a)
b = input("Nhap vao b: ")
b = int(b)
def UCLN(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def BCNN(a, b):
    return (a * b) // UCLN(a, b)
print("Boi chung nho nhat la:", int(BCNN(a, b)))
#cau7
a = input("Nhap so a: ")
a = int(a)
b = input("Nhap so b: ")
b = int(b)
c = input("Nhap so c: ")
c = int(c)
def min(a,b,c):
    min = a
    if b < min:
        min = b
    elif c < min:
        min = c
    print(f"min = {min}")
def max(a,b,c):
    max = a
    if b > max:
        max = b
    elif c > max:
        max = c
    print(f"max = {max}")
min(a,b,c)
max(a,b,c)
#cau8
import math
R = input("Nhap ban kinh : ")
R = int(R)
def tinh_chuvi(R):
    cv = math.pi * 2 * R
    return cv
def tinh_dientich(R):
    S = math.pi * R**2
    return S
print(tinh_chuvi(R))
print(tinh_dientich(R))
#cau9
def tinh_toan(a, b):
    tong = a + b
    hieu = a - b
    tich = a * b    
    print("Tong:", tong)
    print("Hieu:", hieu)
    print("Tich:", tich)
    if b != 0:
        thuong = a / b
        print("Thuong:", thuong)
    else:
        print("Khong the chia cho 0")
a = input("Nhap so a: ")
a = float(a)
b = input("Nhap so b: ")
b = float(b)
tinh_toan(a, b)
#cau10
def uoc_so(n):
    print("Cac uoc so cua", n, "la:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
n = input("Nhap vao n: ")
n = int(n)
uoc_so(n)
#cau11
def nhap():
    ho_ten = input("Nhap ho ten: ")
    toan = input("Nhap diem toan: ")
    toan = float(toan)
    ly = input("Nhap diem ly: ")
    ly = float(ly)
    hoa = input("Nhap diem hoa: ")
    hoa = float(hoa)
    return ho_ten, toan, ly, hoa
def diem_trung_binh(toan, ly, hoa):
    dtb = (toan + ly + hoa) / 3
    return dtb
def xuat(ho_ten,dtb):
    print("Ho ten:", ho_ten)
    print("Điem trung binh:", dtb)
ho_ten, toan, ly, hoa = nhap()
dtb = diem_trung_binh(toan, ly, hoa)
xuat(ho_ten, dtb)
#cau12
def nhap():
    ho_ten = input("Nhap ho ten: ")
    que_quan = input("Nhap que quan: ")
    tham_nien = input("Nhap tham nien cong tac (nam): ")
    tham_nien = int(tham_nien)
    return ho_ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    if tham_nien < 1:
        return 5000000
    elif tham_nien <= 3:
        return 7000000
    else:
        return 10000000
def xuat(ho_ten, que_quan, tham_nien, luong):
    print("Ho ten:", ho_ten)
    print("Que quan:", que_quan)
    print(f"Tham nien cong tac: {tham_nien} nam")
    print("Luong:", luong)
ho_ten, que_quan, tham_nien = nhap()
luong = tinh_luong(tham_nien)
xuat(ho_ten, que_quan, tham_nien, luong)
#cau13
def la_nam_nhuan(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return True
    else:
        return False
def so_ngay_trong_thang(n, x):
    if n in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif n in [4, 6, 9, 11]:
        return 30
    elif n == 2:
        if la_nam_nhuan(x):
            return 29
        else:
            return 28
    else:
        return "Thang khong hop le"
y = input("Nhap vao nam: ")
y = int(y)
m = input("Nhap vao thang: ")
m = int(m)
if la_nam_nhuan(y):
    print(y,"la nam nhuan.")
else:
    print(y,"khong la nam nhuan.")
print("So ngay trong thang:", so_ngay_trong_thang(m, y))
#cau14+15(ý1)
def nhap_danh_sach():
    ds = []
    n = input("Nhap so luong phan tu: ")
    n = int(n)
    for i in range(n):
        x = input(f"Nhap phan tu thu {i+1}: ")
        x = int(x)
        ds.append(x)
    return ds
ds = nhap_danh_sach()
print("Danh sach vua nhap:", ds)
#cau16
def la_so_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
ds_chan = []
for i in range(1, 101):
    if la_so_chan(i):
        ds_chan.append(i)
print("Danh sach so chan:", ds_chan)
#cau17
def la_so_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = input("Nhap vao n: ")
n = int(n)
ds = []
for i in range(n):
    x = input(f"Nhap phan tu thu {i + 1}: ")
    x = int(x)
    ds.append(x)
tong = 0
for i in ds:
    if la_so_chan(i):
        tong = tong + i
print("Danh sach:", ds)
print("Tong cac so chan:", tong)
