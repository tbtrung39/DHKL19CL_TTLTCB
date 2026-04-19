# Bài tập tuần 7:
"""1.Viết chương trình khởi tạo 1 set với các phần tử là kí tự nhập từ bàn phím.
Kết thúc khi người dùng nhập vào "exit". Xóa các phần tử là kí tự số."""
n = input("Nhập các kí tự (nhập 'exit' để kết thúc): ")
s = set()
while n != "exit":
    s.add(n)
    n = input("Nhập các kí tự (nhập 'exit' để kết thúc): ")
for i in list(s):
    if i.isdigit():
        s.remove(i)
print("Set sau khi xóa các phần tử là kí tự số:", s)

"""2. Viết chương trình nhập vào các số tự nhiên từ bàn phím 
và sinh một tập hợp A với các phần tử thuộc danh sách Numbers"""
m = input("Nhập các số tự nhiên: ")
Numbers = m.split()
Numbers = [int(x) for x in Numbers]
A = set(Numbers)
print("Tập hợp A:", A)

"""3. Thống kê chiều cao của hs:"""
ChieuCao = (161, 182, 161, 154, 176, 170, 167, 171, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
            162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170)
# a. Có bao nhiêu sinh viên:
print("Số lượng sinh viên:", len(ChieuCao))
# b. Chiều cao trung bình:
TB = sum(ChieuCao) / len(ChieuCao)
print("Chiều cao trung bình:", TB)
# c. Liệt ra các chiều cao khác nhau trong nhóm và in ra chiều cao trung bình của nhóm:
ChieuCaoKhacNhau = set(ChieuCao)
print("Các chiều cao khác nhau:", ChieuCaoKhacNhau)
print("Chiều cao trung bình của nhóm:", sum(ChieuCaoKhacNhau) / len(ChieuCaoKhacNhau))

"""5. Viết chương trình tạo ra tập hợp A gồm 5 phần tử ngẫu nhiên được lấy từ một
10 phần tử là các số từ 0 đến 9"""
import random
A = set()
while len(A) < 5:
    A.add(random.randint(0, 9))
print("Tập hợp A:", A)

"""6. Viết chương trình thực hiện:"""
# a. Nhập từ bàn phím số tự nhiên:
n = int(input("Nhập một số tự nhiên: "))
# b. In ra màn hình dãy n số nguyên tố đầu tiên:
NguyenTo = []
for i in range(2, n * 10):  
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        NguyenTo.append(i)
    if len(NguyenTo) == n:
        break
print(f"{n} số nguyên tố đầu tiên:", NguyenTo)

"""7. Viết chương trình sinh ngẫu nhiên 2 tập hợp A,B
là các ký tự chữ và số được nhập từ bàn phím sau đó liệt kê các phần tử chung của 2 tập hợp"""
A = set(input("Nhập các ký tự cho tập hợp A: "))
B = set(input("Nhập các ký tự cho tập hợp B: "))
PhanTuChung = A.intersection(B)
print("Các phần tử chung của A và B:", PhanTuChung)

"""8. Viết chương trình sinh tập hợp A gồm cả số nguyên , số thực, chuỗi 
và đếm số phần tử đó."""
A = set()
n = int(input("Nhập số lượng phần tử trong tập hợp A: "))
for _ in range(n):
    element = input("Nhập phần tử (có thể là số nguyên, số thực hoặc chuỗi): ")
    if element.isdigit():
        A.add(int(element))
    else:
        try:
            A.add(float(element))
        except ValueError:
            A.add(element)
print("Tập hợp A:", A)
print("Số phần tử trong tập hợp A:", len(A))

"""9. Viết chương trình thực hiện cv sau:"""
# a. Nhập n vào bàn phím:
n = int(input("Nhập số lượng phần tử trong tập hợp A: "))
# b. Tạo 2 tập hợp A và B , trong đó A là ước của n; tập hợp B bao gồm các số nguyên tố bé hơn n và ko phải ước
A = set()
B = set()
for i in range(1, n + 1):
    if n % i == 0:
        A.add(i)
for i in range(2, n):
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1)) and n % i != 0:
        B.add(i)
print("Tập hợp A (ước của n):", A)
print("Tập hợp B (số nguyên tố bé hơn n và không phải ước):", B)

"""10. Viết chương trình nhập 2 số tự nhiên m,n. Tính tổng các chữ số chung của m và n."""
m = input("Nhập số tự nhiên m: ")
n = input("Nhập số tự nhiên n: ")
Chung = set(m).intersection(set(n))
Tong = sum(int(x) for x in Chung)
print("Tổng các chữ số chung của m và n:", Tong)

"""11. Giả sử có n sinh viên đi thi C++, Java, Python. Các sinh viên được đánh số từ 1 đến n
- Môn C++ có a sinh viên dự thi. Được kí hiệu t1, t2, ..., ta
- Môn Java có b sinh viên dự thi. Được kí hiệu k1, k2, ..., kb
- Môn Python có c sinh viên dự thi. Được kí hiệu h1, h2, ..., hc
Đưa ra 1 danh sách sinh viên chỉ thi 1 ngôn ngữ lập trình, các sinh viên thi 2 ngôn ngữ và các sinh viên thi cả 3 ngôn ngữ."""
n = int(input("Nhập số lượng sinh viên: "))
a = int(input("Nhập số sinh viên thi C++: "))
b = int(input("Nhập số sinh viên thi Java: "))
c = int(input("Nhập số sinh viên thi Python: "))
C = set(input("Nhập số hiệu sinh viên thi C++ (cách nhau bằng dấu cách): ").split())
Java = set(input("Nhập số hiệu sinh viên thi Java (cách nhau bằng dấu cách): ").split())
Python = set(input("Nhập số hiệu sinh viên thi Python (cách nhau bằng dấu cách): ").split())
ThiMotNgonNgu = (C - Java - Python) | (Java - C - Python) | (Python - C - Java)
ThiHaiNgonNgu = (C & Java - Python) | (C & Python - Java) | (Java & Python - C)
ThiBaNgonNgu = C & Java & Python
print("Sinh viên chỉ thi 1 ngôn ngữ lập trình:", ThiMotNgonNgu)
print("Sinh viên thi 2 ngôn ngữ lập trình:", ThiHaiNgonNgu)
print("Sinh viên thi cả 3 ngôn ngữ lập trình:", ThiBaNgonNgu)   

"""12.Nhập n từ bàn phím tạo ra 1 dictionary chứa (i,i*i) như là 1 số nguyên từ 1 đến n (bao gồm cả 1 và n)
sao đó in ra."""
n = int(input("Nhập một số nguyên n: "))
dictionary = {i: i * i for i in range(1, n + 1)}
print("Dictionary chứa (i, i*i):", dictionary)

"""13. Nhập vào chuỗi kí tự, tạo ra 1 từ điển có các thành phần con là các cặp (K,V)
K là 1 chuỗi con liên tiếp nào đó của W và V là số lần suất hiện của K trong W"""
W = input("Nhập một chuỗi kí tự: ")
dictionary = {}
for i in range(len(W)):
    for j in range(i + 1, len(W) + 1):
        K = W[i:j]
        if K in dictionary:
            dictionary[K] += 1
        else:
            dictionary[K] = 1
print("Từ điển chứa các cặp (K, V):", dictionary)

"""14. Tạo ra 1 từ điển số từ 1 đến 100 và chuỗi nhị phân có gtri"""
dict_binary = {}
for i in range(1, 101):
    # Thuật toán chuyển số thập phân sang nhị phân thủ công
    n = i
    s = ""
    if n == 0: s = "0"
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    dict_binary[i] = s

print("Bài 14 (5 phần tử đầu):")
for i in range(1, 6):
    print(f"{i}: {dict_binary[i]}")

# Bài 15
list1 = [101, 102, 103]
list2 = ["An", "Bình", "Chi"]
res_dict = {}

n = len(list1) if len(list1) < len(list2) else len(list2)
for i in range(n):
    res_dict[list1[i]] = list2[i]

print("\nBài 15:")
for k in res_dict:
    print(f"<{k}>: <{res_dict[k]}>")

# Bài 16:
a = [1, 2, 3, 2, 4]
n = len(a)
count = 0
print("\nBài 16:")
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            count += 1
            print(f"Cặp ({i}, {j}): {a[i]} + 1 = {a[j]}")
print(f"Tổng số cặp: {count}")

# Bài 17:
n = int(input("\nNhập số lượng SV (Bài 17): "))
ds_sv = []

for i in range(n):
    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))
    # Làm tròn thủ công: cộng 0.5 rồi lấy phần nguyên
    diem_int = int(diem + 0.5)
    ds_sv.append({'ma': ma, 'ten': ten, 'diem': diem_int})

for i in range(len(ds_sv)):
    for j in range(0, len(ds_sv) - i - 1):
        if ds_sv[j]['diem'] < ds_sv[j+1]['diem']:
            # Hoán vị
            ds_sv[j], ds_sv[j+1] = ds_sv[j+1], ds_sv[j]

print("Danh sách sau sắp xếp:")
for sv in ds_sv:
    print(sv)

# Bài 18:
# Giả sử đã có từ điển data_thi
data_thi = {"001": {"ten": "An", "diem": 8}, "002": {"ten": "Ba", "diem": 7}}
sbd = input("\nNhập SBD cần tra (Bài 18): ")

found = False
for k in data_thi:
    if k == sbd:
        print(f"Họ tên: {data_thi[k]['ten']}, Điểm: {data_thi[k]['diem']}")
        found = True
        break

if not found:
    print("Không tìm thấy, vui lòng nhập mới:")
    ten_moi = input("Họ tên: ")
    diem_moi = float(input("Điểm: "))
    data_thi[sbd] = {"ten": ten_moi, "diem": diem_moi}

# Bai 19:
# a. Tạo mới
n = int(input("\nNhập số NV (Bài 19): "))
nv_dict = {}
for _ in range(n):
    ma = input("Mã NV (4 ký tự): ")
    nv_dict[ma] = {
        "ten": input("Tên: "),
        "nam_sinh": int(input("Năm sinh: ")),
        "luong": float(input("Lương: "))
    }

# b. Thêm nhân viên
ma_them = input("Nhập mã NV cần thêm: ")
nv_dict[ma_them] = {"ten": "Mới", "nam_sinh": 2000, "luong": 5000000}

# c. Tìm kiếm nhân viên tên x
x = input("Nhập tên cần tìm: ")
for ma in nv_dict:
    if nv_dict[ma]['ten'] == x:
        print(f"Tìm thấy mã: {ma}")

# d. Tăng lương cho mã y
y = input("Nhập mã y để tăng lương: ")
if y in nv_dict:
    nv_dict[y]['luong'] += 1000000

# e. Xóa nhân viên mã z
z = input("Nhập mã z để xóa: ")
if z in nv_dict:
    del nv_dict[z]

# f. Sắp xếp giảm dần theo năm sinh (Chuyển sang list để sắp xếp)
ds_nv = []
for ma in nv_dict:
    item = nv_dict[ma]
    item['ma'] = ma
    ds_nv.append(item)

for i in range(len(ds_nv)):
    for j in range(0, len(ds_nv) - i - 1):
        if ds_nv[j]['nam_sinh'] < ds_nv[j+1]['nam_sinh']:
            ds_nv[j], ds_nv[j+1] = ds_nv[j+1], ds_nv[j]

print("Kết quả sắp xếp năm sinh giảm dần:")
for nv in ds_nv:
    print(nv)
