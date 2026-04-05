# Bài tạp về nhà tuần 5:

#============================================================
# Bài 1: Nhập vào bàn phím chuỗi kí tự => đếm số các kí tự là số trong chuỗi và in ra
Chuoi = input("Nhập chuỗi:")
dem = 0
for i in range(len(Chuoi)):
    if Chuoi[i].isdigit(): # isdigit là hàm kiểm tra xem kí tự có phải là số hay không
        dem += 1
print("Số các kí tự là số trong chuỗi là:", dem)

#============================================================
# Bai 2: Nhập vào bàn phím một chuỗi kí tự => có bao nhiêu kí tự không phải là chữ cái tiếng anh và không là chữ số
chuoi = input("Nhập chuỗi:")
tong = 0
for i in range(len(chuoi)):
    if not chuoi[i].isalpha() and not chuoi[i].isdigit():
        tong += 1
print("Số các kí tự không phải là chữ cái tiếng anh và không phải là chữ số là:", tong)

#============================================================
# Bài 3: Nhập vào bàn phím một số tự nhiên => Chuyển từ 10 sang nhị phân và kết quả là chuỗi nhị phân:
n = int(input("Nhập số tự nhiên:"))
chuoi = ""
while n > 0:
    du = n % 2
    chuoi = str(du) + chuoi
    n = n // 2
print("Số nhị phân là:", chuoi)

#============================================================
# Bài 4: Cho trước 2 chuỗi kí tự Str1, Str2 => Viết chương trình xâu chuỗi kí tự 1 và 2, trong đó:
# Từ trái sang phải, từ Str1 đến Str2
# Nếu 1 trong 2 chuỗi kết thúc chỉ cần ghi tiếp phần còn lại của chuỗi còn lại.
Str1 = input("Nhập chuỗi 1:")
Str2 = input("Nhập chuỗi 2:")
chuoi = ""
i = 0
while i < len(Str1) and i < len(Str2):
    chuoi += Str1[i] + Str2[i]
    i += 1
if i < len(Str1):
    chuoi += Str1[i:]
elif i < len(Str2):
    chuoi += Str2[i:]
print("Chuỗi kết quả là:", chuoi)

#============================================================
# Bài 5: Nhập vào bàn phím một chuỗi kí tự => Xóa tất cả Str không phải là số, chuỗi kí tự còn lại là số, trong đó:
# Ktra chuỗi đó có phải là số hoàn hảo không.
chuoi = input("Nhập chuỗi:")
so = ""
for i in range(len(chuoi)):
    if chuoi[i].isdigit():
        so += chuoi[i]

n = int(so)
tong = 0
for i in range(1, n):
    if n % i == 0:
        tong += i
if tong == n:
    print("Số hoàn hảo")
else:
    print("Không phải số hoàn hảo")

#============================================================
# Bài 6: Nhập vào bàn phím một chuỗi kí tự => Ktra xem nó có đc viết trong hệ Hex(0,1,...,9,A,B,C,D,E,F) hay không?
# Nếu có thì loại bỏ dư thừa ko phải Hex 
# Ktra xem chuỗi đó có phải là số hoàn hảo không.
Chuoi = input("Nhập chuỗi:")
hex = "0123456789ABCDEF"
so = ""
for i in range(len(Chuoi)):
    if Chuoi[i] in hex:
        so += Chuoi[i]

n = int(so, 16)
tong = 0
for i in range(1, n):
    if n % i == 0:
        tong += i
if tong == n:
    print("Số hoàn hảo")
else:
    print("Không phải số hoàn hảo")

#============================================================
# Bài 7:(Trùng với bài 5) Nhập vào bàn phím một chuỗi kí tự => Xóa tất cả Str không phải là số, chuỗi kí tự còn lại là số, trong đó:
# Ktra chuỗi đó có phải là số hoàn hảo không.
chuoi = input("Nhập chuỗi:")
so = ""
for i in range(len(chuoi)):
    if chuoi[i].isdigit():
        so += chuoi[i]

n = int(so)
tong = 0
for i in range(1, n):
    if n % i == 0:
        tong += i
if tong == n:
    print("Số hoàn hảo")
else:
    print("Không phải số hoàn hảo")

#============================================================
# Bài 8: Cho 1 xâu Str (có thể nhiều dòng) => Nhập từ đơn để xem trong chuỗi có bao nhiêu lần xuất hiện từ đó
str = input("Nhập chuỗi:")
tu = input("Nhập từ cần tìm:")
dem = 0
for i in range(len(str) - len(tu) + 1):
    if str[i:i+len(tu)] == tu:
        dem += 1
print("Số lần xuất hiện của từ đó là:", dem)

#============================================================
# Bài 9: Nhập vào bàn phím một chuỗi kí tự => Tìm 1 chuỗi con có độ dài lớn nhất trong chuỗi đó và bao gồm các phần tử giống nhau
chuoii = input("Nhập chuỗi:")
len_max = 0
chuoi_max = ""
i = 0
while i < len(chuoii):
    j = i
    while j < len(chuoii) and chuoii[j] == chuoii[i]:
        j += 1
    if j - i > len_max:
        len_max = j - i
        chuoi_max = chuoii[i:j]
    i = j
print("Chuỗi con có độ dài lớn nhất là:", chuoi_max)

#============================================================
# Bài 10: Nhập vào bàn phím một chuỗi kí tự Str1 và Str2 => Tìm kí tự chung cực đại của 2 chuỗi
STR1 = input("Nhập chuỗi 1:")
STR2 = input("Nhập chuỗi 2:")
chuoi = ""
for i in range(len(STR1)):
    for j in range(len(STR2)):
        if STR1[i] == STR2[j] and STR1[i] not in chuoi:
            chuoi += STR1[i]
print("Kí tự chung cực đại của 2 chuỗi là:", chuoi)

#============================================================
# Bài 11: Cho trước chuỗi nhịp phân => Chuyển sang hệ 10
chuoi = input("Nhập chuỗi nhị phân:")
n = 0
for i in range(len(chuoi)):
    n = n * 2 + int(chuoi[i])
print("Số thập phân là:", n)

#============================================================
# Bài 12: Cho chuỗi Str1 => Gọi 1 từ trong chuỗi là 1 dãy kí tự được cách bởi dấu cách
stR = input("Nhập chuỗi:")
tu = input("Nhập từ cần tìm:")
dem = 0
i = 0
while i < len(stR):
    while i < len(stR) and stR[i] == " ":
        i += 1
    j = i
    while j < len(stR) and stR[j] != " ":
        j += 1
    if stR[i:j] == tu:
        dem += 1
    i = j
print("Số lần xuất hiện của từ đó là:", dem)

#============================================================
# Bài 13: Nhập vào 2 chuôi kis tự A,B (chỉ chứa sô 0,1,2..,9) => Chèn thêm + vào giữa 2 số đó => Tính tổng của 2 số, dạng C+D=E+F
# Trường hợp không có thì báo "Không tồn tại cách đặt"
A = input("Nhập chuỗi A:")
B = input("Nhập chuỗi B:")
tong = int(A) + int(B)
tong_str = str(tong)
if len(tong_str) == len(A) + len(B):
    print(A + "+" + B + "=" + tong_str)
else:
    print("Không tồn tại cách đặt")
    