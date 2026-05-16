#1
tap_hop = set()
while True:
    tam = input("Nhập ký tự (nhập 'ESC' để dừng): ")
    if tam == "ESC":
        break
    tap_hop.add(tam)
ket_qua = set()
for x in tap_hop:
    if not x.isdigit():
        ket_qua.add(x)
print(ket_qua)

#2
numbers = [5, 2, 9, 1, 5, 2] # Ví dụ danh sách
A = set(numbers)
min_val = 999999
max_val = -999999
tong = 0
for x in A:
    if x < min_val: min_val = x
    if x > max_val: max_val = x
    tong = tong + x

print("Nhỏ nhất:", min_val, "Lớn nhất:", max_val, "Tổng:", tong)

#4
h = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
dem = 0
for sv in h:
    dem = dem + 1
print("Số sinh viên:", dem)
tong_h = 0
for sv in h:
    tong_h = tong_h + sv
print("Trung bình:", tong_h / dem)
khac_nhau = set(h)
print("Các chiều cao duy nhất:", khac_nhau)

#5
import random
A = set()
while len(A) < 5:
    A.add(random.randint(0, 9))
print("Tập A:", A)

#6
n = int(input("Nhập n: "))
count = 0
so = 2
while count < n:
    la_so_nt = True
    for i in range(2, so):
        if so % i == 0:
            la_so_nt = False
    if la_so_nt:
        print(so)
        count = count + 1
    so = so + 1
    
#7
A = {1, 2, 3, "a"}
B = {3, 4, "a", "b"}
chung = set()
for x in A:
    if x in B:
        chung.add(x)
print("Chung:", chung)

#8
A = {1, 2.5, 3, 4.8, "hello"}
nguyen = 0
thuc = 0
for x in A:
    if type(x) == int:
        nguyen = nguyen + 1
    if type(x) == float:
        thuc = thuc + 1
print("Số nguyên:", nguyen, "Số thực:", thuc)

#9
n = int(input("Nhập n: "))
A = set()
for i in range(2, n + 1):
    if n % i == 0: 
        la_nt = True
        for j in range(2, i):
            if i % j == 0: la_nt = False
        if la_nt: A.add(i)
print("Ước nguyên tố:", A)

#10
m = "1123499"
n = "112229"
set_m = set(m)
set_n = set(n)
tong = 0
for chu_so in set_m:
    if chu_so in set_n:
        tong = tong + int(chu_so)
print("Tổng chữ số chung:", tong)

#11
cpp = {1, 2, 5}
java = {2, 3, 5}
python = {5, 6}

tat_ca = cpp | java | python
print("Danh sách tất cả SV:", tat_ca)

#12
n = int(input("Nhập n: "))
d = {}
for i in range(1, n + 1):
    d[i] = i * i
print(d)

#!3
tudien = {"apple": 0, "banana": 0}
chu_cai = "a"
for tu in tudien:
    dem = 0
    for ky_tu in tu:
        if ky_tu == chu_cai:
            dem = dem + 1
    tudien[tu] = dem
print(tudien)

#14
d = {}
for i in range(1, 101):
    d[i] = bin(i)
print(d)

#15
L1 = ["Ten1", "Ten2", "Ten3"]
L2 = ["An", "Ba", "Ca"]
d = {}
for i in range(len(L1)):
    d[L1[i]] = L2[i]
print(d)

#16
a = [1, 2, 3, 2, 4]
for i in range(len(a)):
    for j in range(len(a)):
        if i < j:
            if a[i] + 1 == a[j]:
                print("Cặp chỉ số:", i, j)

#17
chuoi = "hoc hoc nua hoc mai"
danh_sach_tu = chuoi.split()
tudien = {}
for tu in danh_sach_tu:
    if tu in tudien:
        tudien[tu] = tudien[tu] + 1
    else:
        tudien[tu] = 1
print(tudien)

#18
d = {"A": 1, "B": 2}
moi = {}
for k in d:
    gia_tri = d[k]
    moi[gia_tri] = k
print(moi)

#19
diem = {"An": 8, "Ba": 10, "Ca": 7}
max_d = -1
nguoi_max = ""
for ten in diem:
    if diem[ten] > max_d:
        max_d = diem[ten]
        nguoi_max = ten
print("Cao nhất là:", nguoi_max, "với", max_d, "điểm")