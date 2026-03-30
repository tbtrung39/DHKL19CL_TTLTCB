#7
s = input("Nhập chuỗi: ")
so = ""
for i in s:
    if i.isdigit():
        so += i
print("Chuỗi số:", so)
tong = 0
for i in so:
    tong += int(i)
print("Tổng:", tong)
temp = tong
sum_uoc = 0
for i in range(1, temp):
    if temp % i == 0:
        sum_uoc += i
if sum_uoc == temp:
    print("Là số hoàn hảo")
else:
    print("Không phải số hoàn hảo")
#8
s = input("Nhập đoạn văn: ")
tu = input("Nhập từ cần tìm: ")
dem = s.count(tu)
print("Số lần xuất hiện:", dem)
#9
s = input("Nhập chuỗi: ")
max_len = 1
cur_len = 1
res = s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            res = s[i] * cur_len
    else:
        cur_len = 1
print("Chuỗi con dài nhất:", res)
#10
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
res = ""
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(res):
            res = sub
print("Chuỗi con chung dài nhất:", res)
#11
s = input("Nhập nhị phân: ")
kq = 0
power = 0
for i in range(len(s)-1, -1, -1):
    kq += int(s[i]) * (2**power)
    power += 1
print("Thập phân:", kq)
#12
s = input("Nhập chuỗi: ")
words = s.split()
for w in words:
    print(w)
#13
A = input("Nhập A: ")
B = input("Nhập B: ")
found = False
for i in range(1, len(A)):
    a = int(A[:i])
    b = int(A[i:])
    if a + b == int(B):
        print(f"{a}+{b}={B}")
        found = True
        break
if not found:
    print("Không tồn tại cách đặt!")