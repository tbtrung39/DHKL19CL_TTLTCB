# Bài tập tuần 10:
# Bài 1: Viết hàm kiểm tra xem 3 cạnh a, b, c có tạo thành một tam giác hay không? Nếu có thì tính chu vi và diện tích của tam giác đó.
import math
def is_TamGiac(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def ChuviTamGiac(a, b, c):
    return a + b + c

def S_TamGiac(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

#=============================================
# Bài 2: Viết hàm tính chu vi và diện tích của hình vuông khi biết độ dài cạnh a.
def ChuviHinhvuong(a):
    return a * 4
def Dien_tich_hinh_vuong(a):
    return a * a

#=============================================
# Bài 3: Tính chu vi và diện tích của hình chữ nhật khi biết độ dài hai cạnh a và b.
import math
def Ucln(a, b):
    return math.gcd(a, b)

def Bcnn(a, b):
    return abs(a * b) // math.gcd(a, b)

def SumDivisor(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

#=============================================
# Bài 4: Giải phương trình bậc nhất ax + b = 0 và phương trình bậc hai ax^2 + bx + c = 0.
import math
def giai_bac_nhat(a, b):
    return -b / a if a != 0 else None

def giai_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0: return None
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2
    
#=============================================
# Bài 5: chuyển đổi số đã nhập sang nhị phân, bát phân, thấp phân:
def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_octal(n):
    return oct(n)[2:]

def decimal_to_hexadecimal(n):
    return hex(n)[2:]

#=============================================
# Bài 6: Chuyển đổi từ 2 sang 10, từ 8 sang 10, từ 16 sang 10:
def binary_to_decimal(s):
    return int(s, 2)

def octal_to_decimal(s):
    return int(s, 8)

def hexadecimal_to_decimal(s):
    return int(s, 16)

#=============================================
# Bài 7: Tạo một list gồm 100 số nguyên ngẫu nhiên từ 1 đến 100. Tìm tất cả các số chia hết cho 7.
import random, math
day = [random.randint(1, 100) for _ in range(100)]
chia_het_7 = [x for x in day if x % 7 == 0]
tong_le = sum(x for x in day if x % 2 != 0)
chinh_phuong = [x for x in day if math.isqrt(x)**2 == x]

#=============================================
# Bài 8: Ma trận vuông n x n, in ma trận, chuyển vị ma trận và kiểm tra xem ma trận có đối xứng hay không. 
def nhap_matran(n):
    return [[int(input(f"Nhập A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

def in_matran(mt):
    for row in mt: print(row)

def chuyen_vi(mt):
    return [[mt[j][i] for j in range(len(mt))] for i in range(len(mt))]

def doi_xung(mt):
    return mt == chuyen_vi(mt)

