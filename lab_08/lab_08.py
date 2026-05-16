#1
def value(x):
    return x + 1

n = int(input("Nhập một số nguyên: "))
ket_qua = value(n)
print("Số kế tiếp là:", ket_qua)

#2
def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu, mau):
    ucln = tim_ucln(tu, mau)
    return tu // ucln, mau // ucln

t = int(input("Nhập tử số: "))
m = int(input("Nhập mẫu số: "))
t_moi, m_moi = rut_gon_phan_so(t, m)
print(f"Phân số rút gọn: {t_moi}/{m_moi}")

#3
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

n = int(input("Nhập n: "))
print(f"Các số nguyên tố nhỏ hơn {n}:")
for i in range(2, n):
    if la_so_nguyen_to(i):
        print(i, end=" ")

#4
def lap_phuong(x):
    return x ** 3

n = int(input("Nhập một số: "))
print("Giá trị lập phương:", lap_phuong(n))

#5
def tim_ucln(a, b):
    while b != 0:
        so_du = a % b
        a = b
        b = so_du
    return a
num1 = int(input("Nhập số thứ nhất (a): "))
num2 = int(input("Nhập số thứ hai (b): "))

kq_ucln = tim_ucln(num1, num2)
print(f"Ước chung lớn nhất của {num1} và {num2} là: {kq_ucln}")

#6
def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def tim_bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    ucln = tim_ucln(a, b)
    # Công thức: (a * b) / UCLN
    bcnn = abs(a * b) // ucln
    return bcnn
num1 = int(input("Nhập số thứ nhất (a): "))
num2 = int(input("Nhập số thứ hai (b): "))

kq_bcnn = tim_bcnn(num1, num2)
print(f"Bội chung nhỏ nhất của {num1} và {num2} là: {kq_bcnn}")

#7
def tim_min_max(a, b, c):
    nho_nhat = min(a, b, c)
    lon_nhat = max(a, b, c)
    return nho_nhat, lon_nhat

x, y, z = map(int, input("Nhập 3 số (cách nhau khoảng trắng): ").split())
nho, lon = tim_min_max(x, y, z)
print(f"Số nhỏ nhất: {nho}, Số lớn nhất: {lon}")

#8
import math

def tinh_hinh_tron(r):
    chu_vi = 2 * math.pi * r
    dien_tich = math.pi * (r ** 2)
    return chu_vi, dien_tich

r = float(input("Nhập bán kính: "))
cv, dt = tinh_hinh_tron(r)
print(f"Chu vi: {cv:.2f}, Diện tích: {dt:.2f}")

#9
def tinh_toan(a, b):
    print(f"Cộng: {a + b}")
    print(f"Trừ: {a - b}")
    print(f"Nhân: {a * b}")
    if b != 0:
        print(f"Chia: {a / b}")
    else:
        print("Không thể chia cho 0")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
tinh_toan(a, b)

#10
def in_uoc_so(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

n = int(input("Nhập số nguyên dương n: "))
in_uoc_so(n)

#11
def nhap_sv():
    ten = input("Họ tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    return ten, toan, ly, hoa

def tinh_tb(t, l, h):
    return (t + l + h) / 3

def xuat_sv(ten, tb):
    print(f"Sinh viên {ten} có điểm TB là: {tb:.2f}")

ten, t, l, h = nhap_sv()
tb = tinh_tb(t, l, h)
xuat_sv(ten, tb)

#12
def nhap_nv():
    ten = input("Họ tên: ")
    que = input("Quê quán: ")
    nam = int(input("Thâm niên (năm): "))
    return ten, que, nam

def tinh_luong(nam):
    return 5000000 + (nam * 500000)

def xuat_nv(ten, que, nam, luong):
    print(f"NV: {ten} | Quê: {que} | Thâm niên: {nam} năm | Lương: {luong:,} VNĐ")

ten, que, nam = nhap_nv()
luong = tinh_luong(nam)
xuat_nv(ten, que, nam, luong)

#13
def la_nam_nhuan(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def so_ngay_trong_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]: return 31
    if m in [4, 6, 9, 11]: return 30
    if m == 2:
        return 29 if la_nam_nhuan(y) else 28
    return 0

y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))
print(f"Tháng {m}/{y} có {so_ngay_trong_thang(m, y)} ngày.")

#14
n = int(input("14. Nhập số lượng phần tử n: "))
L = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    L.append(val)
L_binh_phuong = []
for x in L:
    L_binh_phuong.append(x**2)
print("Danh sách bình phương:", L_binh_phuong)

#15
n = int(input("15. Nhập số lượng phần tử n: "))
L = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    L.append(val)
L_le_binh_phuong = []
for x in L:
    if x % 2 != 0: 
        L_le_binh_phuong.append(x**2)

print("Bình phương các số lẻ:", L_le_binh_phuong)

#16
L_chan = []
for i in range(1, 101):
    if i % 2 == 0:
        L_chan.append(i)
print("Danh sách số chẵn từ 1 đến 100:")
print(L_chan)

#17
n = int(input("17. Nhập n: "))
L = []
for i in range(1, n + 1):
    L.append(i)
tong_chan = 0
for x in L:
    if x % 2 == 0:
        tong_chan = tong_chan + x

print(f"Tổng các số chẵn từ 1 đến {n} là: {tong_chan}")