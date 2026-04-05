#bai1
s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if c.isdigit():
        dem += 1
print("Số ký tự là số: ", dem)
#bai2
s = input("Nhập chuỗi: ")
dem = 0
for c in s:
    if not c.isalpha() and not c.isdigit():
        dem += 1
print("Số ký tự đặc biệt: ", dem)
#bai3
n = int(input("Nhập số n: "))
kq = ""
while n > 0:
    kq = str(n % 2) + kq
    n //= 2
print("Nhị phân: ", kq)
#bai4
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
kq = ""
i = 0
while i < len(s1) or i < len(s2):
    if i < len(s1):
        kq += s1[i]
    if i < len(s2):
        kq += s2[i]
    i += 1
print("Chuỗi trộn: ", kq)
#bai5
s = input("Nhập chuỗi: ")
# Lấy các chữ số 
so = ""
for c in s:
    if c.isdigit():
        so += c
print("Chuỗi số: ", so)

# Kiểm tra số hoàn hảo
if so != "":
    n = int(so)
    tong = 0
    for i in range(1,n):
        if n % i == 0:
            tong += i
    if tong == n:
        print("Là số hoàn hảo")
    else:
        print("Không phải là số hoàn hảo")
#bai6
s = input("Nhập chuỗi: ").upper
hex_chars = "0123456789ABCDEF"
hop_le = True
for c in s:
    if c not in hex_chars:
        hop_le = False
if hop_le:
    print("Là chuỗi Hex")
    print("Giá trị thập phân: ", int(s, 16))
else:
    s_moi = ""
    for c in s:
        if c in hex_chars:
            s_moi += c
    print("Chuỗi sau khi lọc: ", s_moi)
    if s_moi != "":
        print("Thập phân: ", int(s_moi, 16))
#bai7
s = input("Nhập chuỗi: ")
# Lấy các chữ số 
so = ""
for c in s:
    if c.isdigit():
        so += c
print("Chuỗi số: ", so)

# Kiểm tra số hoàn hảo
if so != "":
    n = int(so)
    tong = 0
    for i in range(1,n):
        if n % i == 0:
            tong += i
    if tong == n:
        print("Là số hoàn hảo")
    else:
        print("Không phải là số hoàn hảo")
#bai8
text = input("Nhập đoạn văn: ")
word = input("Nhập từ cần tìm: ")
ds = text.split()
dem = 0
for w in ds:
    if w == word:
        dem += 1
print("Số lần xuất hiện: ", dem)
#bai9
s = input("Nhập chuỗi: ")
max_str = ""
cur = s[0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        cur += s[i]
    else:
        if len(cur) > len(max_str):
            max_str = cur
            cur = s[i]
if len(cur) > len(max_str):
    max_str = cur
print("Chuỗi con dài nhất: ", max_str)
#bai10
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
max_str = ""
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(max_str):
            max_str = sub
print("Chuỗi con chung dài nhất: ", max_str)
#bai11
s = input("Nhập chuỗi nhị phân: ")
tong = 0
mu = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == '1':
        tong += 2**mu
    mu += 1
print("Thập phân: ", tong)
#bai12
s = input("Nhập chuỗi: ")
# Thay dấu phẩy bằng khoảng trắng
s = s.replace(",", " ")
words = s.split()
for w in words:
    print(w)
#bai13
A = input("Nhập A: ")
B = input("Nhập B: ")
tim_duoc = False
# Chia A
for i in range(1, len(A)):
    C = int(A[:i])
    D = int(A[:i])
# Chia B
    for j in range(1, len(B)):
        E = int(B[:j])
        F = int(B[i:])
        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            tim_duoc = True
            break
    if tim_duoc:
        break
if not tim_duoc:
    print("Không tồn tại cách đặt")
