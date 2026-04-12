#5
def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n

s = input("Nhập chuỗi: ")
so = ''.join(ch for ch in s if ch.isdigit())
print("Chuỗi số:", so)
if so != "":
    n = int(so)
    if la_so_hoan_hao(n):
        print("Là số hoàn hảo")
    else:
        print("Không phải số hoàn hảo")
else:
    print("Không có số trong chuỗi")
#6
s = input("Nhập chuỗi: ").upper()
hex_chars = "0123456789ABCDEF"
filtered = ''.join(ch for ch in s if ch in hex_chars)
print("Chuỗi sau khi lọc:", filtered)
if filtered != "":
    decimal = int(filtered, 16)
    print("Đổi sang thập phân:", decimal)
else:
    print("Không có ký tự hex hợp lệ")
#7
def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n

s = input("Nhập chuỗi: ")
so = ''.join(ch for ch in s if ch.isdigit())
print("Chuỗi số:", so)
if so != "":
    n = int(so)
    print("Là số hoàn hảo" if la_so_hoan_hao(n) else "Không phải số hoàn hảo")
else:
    print("Không có số")
#8
s = input("Nhập đoạn văn: ")
tu_can_tim = input("Nhập từ cần tìm: ")
words = s.split()
dem = sum(1 for w in words if w == tu_can_tim)
print("Số lần xuất hiện:", dem)
#9
s = input("Nhập chuỗi: ")
max_sub = ""
current = s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        current += s[i]
    else:
        if len(current) > len(max_sub):
            max_sub = current
        current = s[i]
if len(current) > len(max_sub):
    max_sub = current
print("Chuỗi con dài nhất:", max_sub)
#10
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[""] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + s1[i]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)
    return dp[m][n]
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
print("Chuỗi con chung dài nhất:", lcs(s1, s2))
#11
s = input("Nhập chuỗi nhị phân: ")
if all(ch in '01' for ch in s):
    decimal = int(s, 2)
    print("Sang thập phân:", decimal)
else:
    print("Không phải chuỗi nhị phân hợp lệ")
#12
import re
s = input("Nhập chuỗi: ")
words = re.split(r"[,\s]+", s)
for w in words:
    if w != "":
        print(w)
#13
from itertools import product

def tach_so(s):
    n = len(s)
    for mask in product([0, 1], repeat=n-1):
        expr = s[0]
        for i in range(n-1):
            if mask[i] == 1:
                expr += "+"
            expr += s[i+1]
        yield expr
A = input("Nhập A: ")
B = input("Nhập B: ")
found = False
for exprA in tach_so(A):
    for exprB in tach_so(B):
        valA = eval(exprA)
        valB = eval(exprB)
        for a in exprA.split('+'):
            for b in exprA.split('+'):
                pass

        if valA == valB:
            print(f"{exprA} = {exprB}")
            found = True
            break
    if found:
        break
if not found:
    print("Không tồn tại cách đặt!")