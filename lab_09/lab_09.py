#1
def tim_max(n):
    if len(n) == 1:
        return n[0]

    flag = tim_max(n[1:])
    if flag > n[0]:
        return flag
    else:
        return n[0]

n = [int(x) for x in input("Nhập vào một dãy số: ").split()]
print(n)
print("Số lớn nhất trong dãy là:", tim_max(n))
#2
def uc(a, b):
    return a if b == 0 else uc(b, a % b)

def ucln(n):
    if len(n) == 1:
        return n[0]
    return uc(n[0], ucln(n[1:]))

lst = [int(x) for x in input("Nhập các số (cách nhau bằng dấu cách): ").split()]
print("Ước chung lớn nhất là:", ucln(lst))
#3
def tlt(a, n):
    if n == 0:
        return 1
    return a * tlt(a, n - 1)

a = int(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))

print(f"Kết quả {a}^{n} là:", tlt(a, n))
#4
def quay_lui_hoan_vi(hoan_vi_hien_tai, da_xet, n):
    if len(hoan_vi_hien_tai) == n:
        print(hoan_vi_hien_tai)
        return

    for so in range(1, n + 1):
        if not da_xet[so]:
            da_xet[so] = True 
            quay_lui_hoan_vi(hoan_vi_hien_tai + [so], da_xet, n)
            da_xet[so] = False 

n = int(input("Nhập số tự nhiên n: "))
da_xet = [False] * (n + 1)

print(f"Các hoán vị của dãy từ 1 đến {n} là:")
quay_lui_hoan_vi([], da_xet, n)
#5
def permutation(n):
    if n == 1:
        return [[1]]
    
    hoan_vi_truoc = permutation(n - 1)
    ket_qua_moi = []
    
    for mien in hoan_vi_truoc:
        for vi_tri in range(len(mien) + 1):
            hoan_vi_moi = mien[:vi_tri] + [n] + mien[vi_tri:]
            ket_qua_moi.append(hoan_vi_moi)
            
    return ket_qua_moi

n = int(input("Nhập số tự nhiên n: "))
danh_sach_hoan_vi = permutation(n)

print(f"Hàm trả về danh sách gồm {len(danh_sach_hoan_vi)} phần tử:")
print(danh_sach_hoan_vi)
#6
import random

n = int(input("Nhập số tự nhiên n: "))

day_A = list(range(1, n + 1))
ket_qua = []

while len(day_A) > 0:
    so_ngau_nhien = random.choice(day_A)
    
    ket_qua.append(so_ngau_nhien)
    
    day_A.remove(so_ngau_nhien)

print("Dãy result sau khi thiết lập là:", ket_qua)
#7
def quay_lui_tim_nghiem(tong_con_lai, so_luong_con_lai, gia_tri_truoc, nghiem_hien_tai):
    if so_luong_con_lai == 0:
        if tong_con_lai == 0:
            print(" + ".join(map(str, nghiem_hien_tai)))
        return

    if tong_con_lai < 0:
        return

    for so_chon in range(gia_tri_truoc, tong_con_lai + 1):
        quay_lui_tim_nghiem(
            tong_con_lai - so_chon,
            so_luong_con_lai - 1,
            so_chon,
            nghiem_hien_tai + [so_chon]
        )

N = int(input())
n = int(input())
quay_lui_tim_nghiem(N, n, 1, [])
#8
#a
def tinh_tong_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_tong_a(n - 1)

n = int(input())
print(tinh_tong_a(n))

#b
def tinh_giai_thua(k):
    if k == 0 or k == 1:
        return 1
    return k * tinh_giai_thua(k - 1)

def tinh_tong_b(n):
    if n == 1:
        return 1 / tinh_giai_thua(1)
    return 1 / tinh_giai_thua(n) + tinh_tong_b(n - 1)

n = int(input())
print(tinh_tong_b(n))

#c
import math

def tinh_can_c(n, hien_tai=1):
    if hien_tai == n:
        return math.sqrt(3 * n)
    return math.sqrt(3 * hien_tai + tinh_can_c(n, hien_tai + 1))

n = int(input())
print(tinh_can_c(n))

#d
def tinh_can_d(n, hien_tai=1):
    if hien_tai == n:
        return (n + 1) ** (1 / (n + 1))
    return (hien_tai + tinh_can_d(n, hien_tai + 1)) ** (1 / (hien_tai + 1))

n = int(input())
print(tinh_can_d(n))
#9
def dao_nguoc_so(so, ket_qua=0):
    if so == 0:
        return ket_qua
    return dao_nguoc_so(so // 10, ket_qua * 10 + so % 10)

n = int(input())
print(dao_nguoc_so(n))
#10
def tinh_x(n):
    if n == 0:
        return 1
    
    tong = 0
    for i in range(n):
        tong += ((n - i) ** 2) * tinh_x(i)
    return tong

n = int(input())
print(tinh_x(n))
#11
def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)

def tinh_tong_s(k):
    tong = 0
    for i in range(1, k + 1):
        dau = (-1) ** (i + 1)
        tong += dau * giai_thua_kep(i)
    return tong

k = int(input())
print(tinh_tong_s(k))
#cau12
def giai_ga_cho(so_ga):
    if so_ga > 36:
        return None
    
    so_cho = 36 - so_ga
    if (so_ga * 2 + so_cho * 4) == 100:
        return so_ga, so_cho
        
    return giai_ga_cho(so_ga + 1)

ket_qua = giai_ga_cho(0)
print(f"Gà: {ket_qua[0]}, Chó: {ket_qua[1]}")