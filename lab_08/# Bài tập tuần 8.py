# Bai tap tuan 8:
""" Câu 1 Viết chương trình in ra màn hình số kế tiếp của số nguyên nhập từ bàn phím,
sử dụng hàm value(x) để tính số kế tiếp và counter để in ra màn hình"""

def value(x):
    return x + 1
def counter(x):
    print(x)

#================================
"""Câu 2: Viết chương trình rút gọn phân số:
- Tìm UCLN của tử và mẫu
- Chia tử và mẫu của phân số vừa tìm đc cho UCLN"""

def ucln(a,b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)
def rutgon(a,b):
    u = ucln(a,b)
    a = a // u
    b = b // u
    return a, b

#================================
"""Câu 3: Viết chương trình in ra các số nguyên tố nhỏ hơn n 
dùng hàm ktra có phải số nguyên tố hay không"""

def test(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def songuyento(n):
    for i in range(2, n):
        if test(i):
            print(i)

#================================
"""Câu 4: Viết phương trình nhập số nguyên của bàn phím
từ đó tìm gtri lập phương."""

def lapphuong(n):
    return n ** 3
n = int(input("Nhập số nguyên: "))
print("Giá trị lập phương của", n, "là:", lapphuong(n))

#================================
"""Câu 5: Viết chương trình tìm UCLL của a,b"""
def ucll(a,b):
    return (a * b) // ucln(a, b)
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print("Ước chung lớn nhất của", a, "và", b, "là:", ucln(a, b))
print("Bội chung nhỏ nhất của", a, "và", b, "là:", ucll(a, b))

#================================
"""Câu 6: Xây dựng chương trình tìm bội chung nhỏ nhất của a,b"""

def boichungnho(a,b):
    return (a * b) // ucln(a, b)
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print("Bội chung nhỏ nhất của", a, "và", b, "là:", boichungnho(a, b))

#================================
"""Câu 8: Viết chương trình tính chu vi và diện tích hình tròn"""

import math
def chuvi(r):
    return 2 * math.pi * r
def dientich(r):
    return math.pi * r ** 2
r = float(input("Nhập bán kính hình tròn: "))
print("Chu vi hình tròn là:", chuvi(r))
print("Diện tích hình tròn là:", dientich(r))

#================================
"""Câu 10. Viết chương trình nhập n và in ra ước của nó"""

def uoc(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
n = int(input("Nhập số nguyên n: "))
print("Các ước của", n, "là:")

#================================
"""Câu 12: Nhập họ tên, quê, thâm niên
- Tính lương dựa vào thâm niên (vd: <5 năm: 5 triệu, 5-10 năm: 7 triệu, >10 năm: 10 triệu)
- Xuất tên họ tên, quê, thâm niên và lương
- viết chương trình nhập thông tin của 1 nhân viên gồm họ tên, quê, thâm niên sử dụng 3 hàm trên"""

def tinhluong(tham_nien):
    if tham_nien < 5:
        return 5000000
    elif tham_nien < 10:
        return 7000000
    else:
        return 10000000
def nhapthongtin():
    ho_ten = input("Nhập họ tên: ")
    que = input("Nhập quê: ")
    tham_nien = int(input("Nhập thâm niên (năm): "))
    return ho_ten, que, tham_nien

def xuatthongtin(ho_ten, que, tham_nien, luong):
    print("Họ tên:", ho_ten)
    print("Quê:", que)
    print("Thâm niên:", tham_nien, "năm")
    print("Lương:", luong, "VND")

ho_ten, que, tham_nien = nhapthongtin()
luong = tinhluong(tham_nien)
xuatthongtin(ho_ten, que, tham_nien, luong)

#================================
"""Câu 13. Viết hàm
- Ktra năm y là nhuận hay không
- Xác định số ngày tối đa của tháng m trong năm y cho trc"""

def nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def ngay(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if nhuan(y):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ"
    
m = int(input("Nhập tháng (1-12): "))
y = int(input("Nhập năm: "))
print("Số ngày tối đa của tháng", m, "năm", y, "là:", ngay(m, y))

#================================
"""Câu 14: Viết chương trình
- Tạo 1 list nhập từ bàn phím
- Sử dụng map và lamda: tạo list chứa bình phương các số hạn của list trên"""

n = int(input("Nhập số lượng phần tử: "))
lst = []
for i in range(n):
    num = int(input("Nhập số nguyên: "))
    lst.append(num)
squared_lst = list(map(lambda x: x ** 2, lst))
print("List chứa bình phương các số nguyên:", squared_lst)

#================================
"""Câu 15: Viết chương trình
- Tạo 1 list nhập từ bàn phím
- Sử dụng map và lamda: tạo list chứa bình phương các số lẻ của list trên"""

n = int(input("Nhập số lượng phần tử: "))
lst = []
for i in range(n):
    num = int(input("Nhập số nguyên: "))
    lst.append(num)
for i in lst:
    if i % 2 != 0:
        print(i ** 2)


#================================
"""Câu 16: Viết list toàn số chẵn từ 1 đến 100"""

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

#================================
"""Câu 17: Nhập 1 ds từ bàn phím, sử dụng filter và reduce viết hàm tính tổng số chẵn """

from functools import reduce
n = int(input("Nhập số lượng phần tử: "))
lst = []
for i in range(n):
    num = int(input("Nhập số nguyên: "))
    lst.append(num)
even_numbers = list(filter(lambda x: x % 2 == 0, lst))
total = reduce(lambda x, y: x + y, even_numbers)
print("Tổng các số chẵn trong list là:", total)


