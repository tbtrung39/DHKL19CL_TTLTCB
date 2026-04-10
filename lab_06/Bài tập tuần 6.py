# Bài tập tuần 6:
# 1. Cho danh sách a = [2,-4,1,9,-3,6,3,-2,6,8] gồm n = 10 phần tử.
# Yêu cầu:
# a. Viết chương chình python tính tổng:
a = [2,-4,1,9,-3,6,3,-2,6,8]
tong = 0
for i in a:
    tong = tong + i
print("Tổng của các phần tử trong danh sách a là:", tong)

# b. Viết chương trình python đếm số lượng các số hạng dương và tổng các số hạng dương:
viet_duong = 0
tong_duong = 0
for i in a:
    if i > 0:
        viet_duong = viet_duong + 1
        tong_duong = tong_duong + i
print("Số lượng các số hạng dương là:", viet_duong)
print("Tổng các số hạng dương là:", tong_duong)
__author__ = "Lê Quốc Việt"
__copyright__ = "Bài tập tuần 6"
__license__ = "MIT"

# c. Tìm vị trí phần tử âm đầu tiên có trong danh sách:
vitri = -1
for i in range(len(a)):
    if a[i] < 0:
        vitri = i
        break
if vitri != -1:
    print("Vị trí phần tử âm đầu tiên trong danh sách a là:", vitri)
else:
    print("Không có phần tử âm nào trong danh sách a.")

# d. Tìm vị trí phần tử dương cuối cùng có trong danh sách:
vitri_duong = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vitri_duong = i
        break
if vitri_duong != -1:
    print("Vị trí phần tử dương cuối cùng trong danh sách a là:", vitri_duong)
else:
    print("Không có phần tử dương nào trong danh sách a.")

# e. Tìm phần tử lớn nhất và vị trí lớn nhất cuối cùng có trong danh sách:
max_value = a[0]
vitri_max = 0
for i in range(1, len(a)):
    if a[i] >= max_value:
        max_value = a[i]
        vitri_max = i
print("Phần tử lớn nhất trong danh sách a là:", max_value)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách a là:", vitri_max)

#============================================
# 2. Nhập từ bàn phím n, trong đó:
# a. Tìm phần tử lớn nhất thứ 32 trong ds và vị trí phần tử lớn nhất đạt vị trí thứ 2:
n = int(input("Nhập số lượng phần tử n: "))
ds = []
for i in range(n):
    vit = int(input("Nhập phần tử thứ {}: ".format(i+1)))
    ds.append(vit)
max_viet = ds[0]
vitri_max = 0
for i in range(1, len(ds)):
    if ds[i] >= max_viet:
        max_viet = ds[i]
        vitri_max = i
print("Phần tử lớn nhất trong danh sách ds là:", max_viet)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách ds là:", vitri_max)

# b. Tính số lượng các số dương liên tiếp nhiều nhất trong ds:
max_duong = 0
quoc_duong = 0
for i in range(len(ds)):
    if ds[i] > 0:
        quoc_duong = quoc_duong + 1
        if quoc_duong > max_duong:
            max_duong = quoc_duong
    else:
        quoc_duong = 0
print("Số lượng các số dương liên tiếp nhiều nhất trong danh sách ds là:", max_duong)

# c. Tính số lượng số dương liên tiếp có tổng max:
maxTongDuong = 0
tongDuong = 0
for i in range(len(ds)):
    if ds[i] > 0:
        tongDuong = tongDuong + ds[i]
        if tongDuong > maxTongDuong:
            maxTongDuong = tongDuong
    else:
        tongDuong = 0
print("Số lượng số dương liên tiếp có tổng max trong danh sách ds là:", maxTongDuong)

#============================================
# 3. Nhập 1 danh sách phần tử cho đến khi nhập vào số 0, trong đó:
# a. Viết các phần tử dương của ds lên dâdu ds và in ra màn hình:
ds = []
while True:
    quocviet = int(input("Nhập phần tử (nhập 0 để kết thúc): "))
    if quocviet == 0:
        break
    ds.append(quocviet)
print("Danh sách phần tử đã nhập:", ds)

print("Các phần tử dương trong danh sách ds là:")
for i in ds:
    if i > 0:
        print(i)

# b. Chèn m nhập từ bàn phím vào đầu vào cuối và vào vị trí thứ 5:
v = int(input("Nhập số m: "))
ds.insert(0, v)  
ds.append(v)    
if len(ds) >= 5:
    ds.insert(4, v) 
print("Danh sách sau khi chèn m vào đầu, cuối và vị trí thứ 5:", ds)

#============================================
# 4. Nhập 1 danh sách phần tử cho đến khi nhập vào số 0, trong đó:
# a. Chèn [1,2,3] vào đầu, cuối, vitri thứ 5 của ds:
ds = []
while True:
    Quocviet = int(input("Nhập phần tử (nhập 0 để kết thúc): "))
    if Quocviet == 0:
        break
    ds.append(Quocviet) 
ds.insert(0, [1, 2, 3])
ds.append([1, 2, 3])
if len(ds) >= 5:
    ds.insert(4, [1, 2, 3])
print("Danh sách sau khi chèn [1, 2, 3] vào đầu, cuối và vị trí thứ 5:", ds)

# b. Xóa phần tử thứ k nhập từ bàn phím:
k = int(input("Nhập vị trí k để xóa phần tử: "))
if 0 <= k < len(ds):
    xoa = ds.pop(k)
    print("Đã xóa phần tử tại vị trí {}: {}".format(k, xoa))
else:
    print("Vị trí k không hợp lệ.")

# c. Sắp xếp theo thứ tự giảm và tăng:
ds.sort()
print("Danh sách sau khi sắp xếp theo thứ tự tăng:", ds)
ds.sort(reverse=True)
print("Danh sách sau khi sắp xếp theo thứ tự giảm:", ds)

#============================================
# 5. Viết 1 list A sinh gồm 1000 số tự nhiên, nằm ngẫu nhiên trong [1,10000]:
import random
A = [random.randint(1, 10000) for _ in range(1000)]
print("List A sinh gồm 1000 số tự nhiên ngẫu nhiên trong [1, 10000]:", A)

#============================================
# 6. Viết 1 list A sinh gồm 1000 số tự nhiên, nằm ngẫu nhiên trong [1,10000], sau đó lm theo 2 cách 1 là có sort(), 2 là không sort():
import random
A = [random.randint(1, 10000) for _ in range(1000)]
print("List A sinh gồm 1000 số tự nhiên ngẫu nhiên trong [1, 10000]:", A)
A.sort()
print("List A sau khi sắp xếp:", A)

#============================================
# 7. Giả sử có 1 list sau: 
List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
# a. Tạo ds list và in ra màn hình:
print("Danh sách List:", List)
# b. Chọn ra phần thứ 2, thuộc vị trí thứ 3 của sublist:
print("Phần tử thứ 2, thuộc vị trí thứ 3 của sublist:", List[2][1])
# c. Kiểm tra độ dài của list test và thêm 1 sublist ngẫu nhiên:
test = [["a", 1], ["b", 2], ["c", 3]]
print("Danh sách test:", test)
print("Độ dài của danh sách test:", len(test))
test.append(["d", 4])
print("Danh sách test sau khi thêm sublist ngẫu nhiên:", test)
# d. Thực hiện tính toán tổng value trong ngày thứ 2,3,7 và cn:
tong = List[1][1] + List[2][1] + List[6][1]
print("Tổng value trong ngày thứ 2, 3, 7 và cn là:", tong)

#============================================
# 8. Nhập từ bàn phím n. Sử dụng comprehension để in ra dãy Fibonacci dưới dạng "'"
q = int(input("Nhập số lượng phần tử n: "))
fib = [0, 1]
for i in range(q - 2):
    fib.append(fib[-1] + fib[-2])
print("Dãy Fibonacci gồm {} phần tử:".format(q), fib)

#============================================
# 9. Viết chương trình sử dụng lệnh assert để xác minh tất cả số trong list là số chẵn:
SoViet  = [2, 4, 6, 8, 10]
for num in SoViet:
    assert num % 2 == 0, "Số {} không phải là số chẵn".format(num)
print("Tất cả số trong list đều là số chẵn.")
# Nhập từ bàn phím:
n = int(input("Nhập số lượng phần tử n: "))
SoViet = []
for i in range(n):
    num = int(input("Nhập phần tử thứ {}: ".format(i+1)))
    SoViet.append(num)
for num in SoViet:
    assert num % 2 == 0, "Số {} không phải là số chẵn".format(num)
print("Tất cả số trong list đều là số chẵn.")

#============================================
# 10. Viết chương trình sử dụng module random và list comprehension, trong đó:
# Chia hết cho 5 và 7, bắt đầu từ 0 đến 200
import random
soviet = [num for num in range(201) if num % 5 == 0 and num % 7 == 0]
print("Các số chia hết cho 5 và 7 từ 0 đến 200:", soviet)

#============================================
# 11. Viết chương trình tạo ra 1 list A sử dụng list comprehension, trong đó:
n = int(input("Nhập số lượng phần tử n: "))
A = [random.randint(1, 100) for _ in range(20)]
# a. Tạo list B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5
B = [num for num in A if num % 3 == 0 and num % 5 != 0]
print("Kết quả:", B)
# b. Tạo ra list C là các phần tử bình phương của list A:
C = [num ** 2 for num in A]
print("List C (bình phương của A):", C)
# c. Tạo ra list D ngẫu nhiên từ ds D mà chia hết cho 3:
D = [num for num in A if num % 3 == 0]
print("List D (các phần tử chia hết cho 3):", D)

#============================================
# 12. Nhập vào giiao diện điều khiển. Viết chương trình thực tính số tiền thực của 1 tài khoản ngân hàng dựa trên nhập kí sau:
""" Định dạng nhật ký:
        D 100 (D là tiền gửi)
        W 200 (W là tiền rút)
    Giả sử đầu vào cung cấp là:
        D 300
        D 300
        W 200
        D 100
        Thì đầu ra là: 500"""

TaiKhoan = 0
while True:
    nhap = input("Nhập nhật ký (D để gửi, W để rút, nhập '0' để kết thúc): ")
    if nhap.lower() == '0':
        break
    try:
        action, amount = nhap.split()
        amount = int(amount)
        if action.upper() == 'D':
            TaiKhoan += amount
        elif action.upper() == 'W':
            TaiKhoan -= amount
        else:
            print("Vui lòng nhập D hoặc W.")
    except ValueError:
        print("Vui lòng nhập theo định dạng 'D 100' hoặc 'W 200'.")
print("Số tiền của tài khoản là:", TaiKhoan)

#============================================
# 13. Viết chương trình tạo ra chủ ngữ ["Anh","Em"], động từ ["Chơi","Yêu"], tân ngữ ["Bóng đá","Cầu rổ"]
ChuNgu = ["Anh", "Em"]
DongTu = ["Chơi", "Yêu"]
TanNgu = ["Bóng đá", "Cầu rổ"]
Cau = [f"{cn} {dt} {tn}" for cn in ChuNgu for dt in DongTu for tn in TanNgu]
print("Các câu được tạo ra:")
for cau in Cau:
    print(cau)

#============================================
# 14. Nhập tên ng dùng và mật khẩu để đki => Viết chương trình, trong đó:
print("Đăng ký tài khoản")
print("Tên người dùng:")
# a. Mật khẩu t nhất 1 chữ cái nằm trong [a-z].
print("Mật khẩu:")
while True:
    mkhau = input("Nhập mật khẩu: ")
    if any(c.isalpha() for c in mkhau):
        print("Đăng ký thành công!")
        break
    else:
        print("Vui lòng thử lại. Mật khẩu phải chứa ít nhất một chữ cái từ a-z.")
# b. Mật khẩu ít nhất 1 chữ số nằm trong [0-9].
while True:
    mkhau = input("Nhập mật khẩu: ")
    if any(c.isdigit() for c in mkhau):
        print("Đăng ký thành công!")
        break
    else:
        print("Vui lòng thử lại. Mật khẩu phải chứa ít nhất một chữ số từ 0-9.")
# c. Mật khẩu ít nhất 1 ký tự đặc biệt nằm trong [A-Z].
while True:
    mkhau = input("Nhập mật khẩu: ")
    if any(c.isupper() for c in mkhau):
        print("Đăng ký thành công!")
        break
    else:
        print("Vui lòng thử lại. Mật khẩu phải chứa ít nhất một ký tự đặc biệt từ A-Z.")
# d. Mật khẩu chứa [$#@].
while True:
    mkhau = input("Nhập mật khẩu: ")
    if any(c in '$#@' for c in mkhau):
        print("Đăng ký thành công!")
        break
    else:
        print("Vui lòng thử lại. Mật khẩu phải chứa ít nhất một ký tự đặc biệt từ $#@.")
# e. Độ dài tối thiểu 6 ký tự.
while True:
    mkhau = input("Nhập mật khẩu: ")
    if len(mkhau) >= 6:
        print("Đăng ký thành công!")
        break
    else:
        print("Vui lòng thử lại. Mật khẩu phải có độ dài tối thiểu 6 ký tự.")

# f. Độ dài tối đa 12 ký tự.
while True:
    mkhau = input("Nhập mật khẩu: ")
    if len(mkhau) <= 12:
        print("Đăng ký thành công!")
        break
    else:
        print("Vui lòng thử lại. Mật khẩu phải có độ dài tối đa 12 ký tự.")

#============================================
# 15. Viết chương trình sắp xếp tuple(name, age, score) theo thứ tự tăng dần, trong đó:
"""Name là string, age và score là số. Tuple được nhập từ bàn phím. Sắp xếp theo name>age>score"""
n = int(input("Nhập số lượng tuple n: "))
tuples = []
for i in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm số: "))
    tuples.append((name, age, score))
sorted_tuples = sorted(tuples, key=lambda x: (x[0], x[1], x[2]))
print("Sau khi sắp xếp:")
for t in sorted_tuples:
    print(t)

#============================================
# Bài 16. Nhập 2 sô X,Y tạo ra 1 mảng 2 chiều. Giá trị hàng thứ i và cột thứ j của màng là i*j
X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))
Mang2chieu = [[i * j for j in range(Y)] for i in range(X)]
print("Mảng 2 chiều:")
for row in Mang2chieu:
    print(row)

#============================================
# 17. Viết chương trình sinh list A là biểu diễn của matrix đơn vị. Nhập n và sinh ra matrix đơn vị bậc n:
__author__ = "Lê Quốc Việt"
__copyright__ = "Bài tập tuần 6"
n = int(input("Nhập kích thước n của ma trận đơn vị: "))
MaTranDonVi = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Ma trận đơn vị bậc {}:".format(n))
for row in MaTranDonVi:
    print(row)

#============================================
# 18. Cho:
"""A=[[a11,a12,..a1n],[a21,a22,..a2n],...,[am1,am2,..amn]]"""
# a. Nhập vào matrix A với aij là số đc nhập:
hang = int(input("Nhập số hàng: "))
cot = int(input("Nhập số cột: "))
A = []
for i in range(hang):
    row = []
    for j in range(cot):
        aij = float(input(f"Nhập a[{i+1}][{j+1}]"))
        row.append(int(aij))
    A.append(row)
print("Ma trận A:")
for row in A:
    print(row)
# Tính tổng các phần tử matrix A:
TongA = 0
for row in A:
    for Viet in row:
        TongA += Viet
print("Tổng:", TongA)

