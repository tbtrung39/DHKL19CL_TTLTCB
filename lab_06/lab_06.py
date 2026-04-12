#4
lst = []
while True:
    n = int(input("Nhập số (0 để dừng): "))
    if n == 0:
        break
    lst.append(n)

print("Danh sách ban đầu:", lst)
add_list = [1, 2, 3]
lst = add_list + lst
print("Sau khi chèn vào đầu:", lst)
lst = lst + add_list
print("Sau khi chèn vào cuối:", lst)
if len(lst) >= 4:
    lst[4:4] = add_list
else:
    lst = lst + add_list
print("Sau khi chèn vào vị trí thứ 5:", lst)
k = int(input("Nhập vị trí k muốn xóa (bắt đầu từ 1): "))
if 1 <= k <= len(lst):
    lst.pop(k - 1)
    print("Sau khi xóa:", lst)
else:
    print("Vị trí không hợp lệ")
lst_tang = sorted(lst)
print("Tăng dần:", lst_tang)
lst_giam = sorted(lst, reverse=True)
print("Giảm dần:", lst_giam)
#5
import random

A = [random.randint(1, 99999) for _ in range(1000)]
print("Danh sách A:")
print(A)
#6
import random

A = [random.randint(1, 99999) for _ in range(1000)]
A_sorted = sorted(A)
print("Sắp xếp bằng sorted():")
print(A_sorted)
B = A.copy()
for i in range(len(B)):
    for j in range(0, len(B) - i - 1):
        if B[j] > B[j + 1]:
            B[j], B[j + 1] = B[j + 1], B[j]
print("Sắp xếp không dùng sorted():")
print(B)
#7
import random

List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Các phần tử trong List_:")
for item in List_:
    print(item)
target_value = List_[2][1]
print(f"\nPhần tử thứ hai của sublist thứ 3 là: {target_value}")
print(f"Độ dài của list hiện tại: {len(List_)}")
new_sublist = ["extra", random.randint(50, 150)]
List_.append(new_sublist)
print(f"List sau khi thêm sublist ngẫu nhiên: {List_}")
target_days = ["mon", "tue", "sat", "sun"]
total_sales = sum(item[1] for item in List_ if item[0] in target_days)
print(f"Tổng sale value của các ngày {target_days} là: {total_sales}")
#8
import math

n = int(input("Nhập n: "))
def fib(i):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**i - psi**i) / math.sqrt(5))
fib_sequence = [str(fib(i)) for i in range(n + 1)]
print(", ". join(fib_sequence))
#9
input_str = input("Nhập danh sách các số, cách nhau bằng dấu cách: ")
numbers = [int(x) for x in input_str.split()]
try:
    for num in numbers:
        assert num % 2 == 0, f"Phát hiện số lẻ: {num}"
    print("Xác minh thành công: Tất cả các số đều là số chẵn.")
except AssertionError as e:
    print(f"Xác minh thất bại! {e}")
#10
import random

candidates = [i for i in range(201) if i % 5 == 0 and i % 7 == 0]
if candidates:
    result = random.choice(candidates)
    print(f"Số ngẫu nhiên thỏa mãn (0-200, chia hết cho 5 và 7): {result}")
else:
    print("Không tìm thấy số nào thỏa mãn.")
#11
import random

n = int(input("Nhập số lượng phần tử n: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
print(f"Danh sách A gốc: {A}")
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(f"a. Danh sách B (chia hết cho 3, không cho 5): {B}")
C = [x**2 for x in A]
print(f"b. Danh sách C (bình phương): {C}")
sub_A = [x for x in A if x % 3 == 0]
if sub_A:
    k = random.randint(1, len(sub_A))
    D = random.sample(sub_A, k)
    print(f"c. Danh sách D (ngẫu nhiên từ các số chia hết cho 3): {D}")
else:
    print("c. Không có phần tử nào trong A chia hết cho 3 để tạo D.")
#12
import sys

def calculate_balance():
    balance = 0
    print("Nhập nhật ký giao dịch (Nhấn Enter trống để kết thúc):")
    
    while True:
        line = input()
        if not line:
            break
        parts = line.split()
        operation = parts[0]
        amount = int(parts[1])
        if operation == 'D':
            balance += amount
        elif operation == 'W':
            balance -= amount
    print(f"Số tiền thực của tài khoản là: {balance}")
if __name__ == "__main__":
    calculate_balance()
#13
subjects = ["Anh", "Em"]
verbs = ["Chơi", "Yêu"]
objects = ["Bóng đá", "Bóng rổ"]
print("Tất cả các câu có thể tạo ra là:")
for sub in subjects:
    for v in verbs:
        for obj in objects:
            sentence = f"{sub} {v} {obj}."
            print(sentence)
#14
import re

def check_password_validity():
    input_str = input("Nhập các mật khẩu cần kiểm tra (cách nhau bởi dấu phẩy): ")
    passwords = [p.strip() for p in input_str.split(",")]

    valid_passwords = []
    for p in passwords:
        if len(p) < 6 or len(p) > 12:
            continue
        if not re.search("[a-z]", p):
            continue
        if not re.search("[A-Z]", p):
            continue
        if not re.search("[0-9]", p):
            continue
        if not re.search("[$#@]", p):
            continue
        valid_passwords.append(p)
    print(",".join(valid_passwords))
if __name__ == "__main__":
    check_password_validity()
#15
data = []
print("Nhập thông tin (name, age, score). Để trống và nhấn Enter để dừng:")
while True:
    s = input()
    if not s:
        break
    parts = s.split(",")
    data.append((parts[0].strip(), int(parts[1].strip()), int(parts[2].strip())))
sorted_data = sorted(data)

print("\nDanh sách sau khi sắp xếp:")
print(sorted_data)
#16
dimensions = input("Nhập X, Y (ví dụ: 3,5): ").split(',')
X = int(dimensions[0])
Y = int(dimensions[1])
matrix = [[i * j for j in range(Y)] for i in range(X)]
print(f"Mảng {X}x{Y} tạo ra là:")
print(matrix)
#17
n = int(input("Nhập bậc của ma trận đơn vị n: "))
identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(f"Ma trận đơn vị bậc {n}:")
for row in identity_matrix:
    print(row)
#18
# Nhập kích thước ma trận
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# a. Viết chương trình nhập vào ma trận A
A = []
print(f"Nhập các phần tử cho ma trận {m}x{n}:")
for i in range(m):
    row = []
    for j in range(n):
        val = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        row.append(val)
    A.append(row)

# Hiển thị ma trận vừa nhập
print("\nMa trận A vừa nhập:")
for row in A:
    print(row)
total_sum = sum(sum(row) for row in A)

print(f"\nTổng tất cả các phần tử trong ma trận là: {total_sum}")