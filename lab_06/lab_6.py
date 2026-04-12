#1
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

tong = sum(a)
print("Tổng các phần tử:", tong)

so_duong = [x for x in a if x > 0]
print("Số lượng số dương:", len(so_duong))
print("Tổng các số dương:", sum(so_duong))

vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)

vi_tri_duong_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)

max_value = max(a)
vi_tri_max = len(a) - 1 - a[::-1].index(max_value)
print("Phần tử lớn nhất:", max_value)
print("Vị trí cuối cùng của phần tử lớn nhất:", vi_tri_max)

#2
n = int(input())
a = list(map(int, input().split()))

b = sorted(set(a), reverse=True)
print("Phần tử lớn thứ hai:", b[1])
print("Vị trí:", a.index(b[1]))

max_len = 0
count = 0
for x in a:
    if x > 0:
        count += 1
        max_len = max(max_len, count)
    else:
        count = 0
print("Số lượng dãy dương liên tiếp dài nhất:", max_len)

max_sum = 0
current_sum = 0
for x in a:
    if x > 0:
        current_sum += x
        max_sum = max(max_sum, current_sum)
    else:
        current_sum = 0
print("Tổng dãy dương liên tiếp lớn nhất:", max_sum)

#3
a = []
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)

duong = [x for x in a if x > 0]
am = [x for x in a if x <= 0]
a = duong + am
print(a)

m = int(input())
a.insert(0, m)
a.append(m)
a.insert(4, m)
print(a)

#4
a = []
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)

a = [1,2,3] + a + [1,2,3]
if len(a) >= 5:
    a = a[:4] + [1,2,3] + a[4:]
print(a)

k = int(input())
if 0 <= k < len(a):
    a.pop(k)
print(a)

print(sorted(a))
print(sorted(a, reverse=True))

#5
import random
a = [random.randint(1,99999) for _ in range(1000)]
print(a)

#6
import random
a = [random.randint(1,99999) for _ in range(1000)]

b = sorted(a)
print(b)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

#7
List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]

print(List_)

print(List_[2][1])

import random
List_.append(["rand", random.randint(1,200)])
print(len(List_))

tong = 0
for day, val in List_:
    if day in ["tue","wed","sat","sun"]:
        tong += val
print(tong)

#8
n = int(input())
fibo = [0,1]
for i in range(2,n+1):
    fibo.append(fibo[-1] + fibo[-2])

print(", ".join(str(fibo[i]) for i in range(n+1)))

#9
a = list(map(int, input().split()))
for x in a:
    assert x % 2 == 0
print("Tất cả đều là số chẵn")

#10
import random
a = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
print(random.sample(a, min(10, len(a))))

#11
n = int(input())
A = list(map(int, input().split()))

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(B)

C = [x*x for x in A]
print(C)

import random
D = random.sample([x for x in A if x % 3 == 0], min(3, len(A)))
print(D)

#12
tong = 0
while True:
    s = input()
    if not s:
        break
    t, v = s.split()
    v = int(v)
    if t == 'D':
        tong += v
    elif t == 'W':
        tong -= v
print(tong)

#13
chu_ngu = ["Anh","Em"]
dong_tu = ["Choi","Yeu"]
tan_ngu = ["Bong da","Bong ro"]

for s in chu_ngu:
    for v in dong_tu:
        for o in tan_ngu:
            print(s, v, o)

#14
import re

passwords = input().split(',')

valid = []
for p in passwords:
    if (6 <= len(p) <= 12 and
        re.search("[a-z]", p) and
        re.search("[A-Z]", p) and
        re.search("[0-9]", p) and
        re.search("[$#@]", p)):
        valid.append(p)

print(",".join(valid))

#15
n = int(input())
a = []

for _ in range(n):
    name, age, score = input().split()
    a.append((name, int(age), int(score)))

a.sort(key=lambda x: (x[0], x[1], x[2]))

for i in a:
    print(i)

#16
X, Y = map(int, input().split())

a = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    a.append(row)

print(a)

#17
n = int(input())

a = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    a.append(row)

for row in a:
    print(row)

#18
m, n = map(int, input().split())

A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

tong = 0
for row in A:
    tong += sum(row)

print("Tổng ma trận:", tong)
