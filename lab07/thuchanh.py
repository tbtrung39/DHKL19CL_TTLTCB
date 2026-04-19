#1
s1 = set()
print("Nhập ký tự (nhập 'stop' để kết thúc):")
while True:
    val = input()
    if val.lower() == 'stop': break
    s1.add(val)
print("Set đã nhập:", s1)
#2
numbers = {int(x) for x in s1 if x.isdigit()}
s1 = s1 - {str(x) for x in numbers}
print("Set số tự nhiên:", numbers)
print("Set sau khi xóa số:", s1)
#3
import random
n = int(input("Nhập n số thực: "))
A = {random.uniform(1, 100) for _ in range(n)}
print("Tập hợp A:", A)
print("Min:", min(A))
print("Max:", max(A))
print("Tổng:", sum(A))
#4
heights = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
# 4a.
print("Số sinh viên:", len(heights))
# 4b.
avg_h = sum(heights) / len(heights)
print("Chiều cao trung bình:", avg_h)
distinct_heights = set(heights)
print("Các chiều cao khác nhau:", sorted(distinct_heights))
#6
n = int(input("Nhập n số nguyên tố đầu tiên: "))
primes = []
num = 2
while len(primes) < n:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime: primes.append(num)
    num += 1
print(f"{n} số nguyên tố đầu tiên:", primes)
#7
import random
A = {random.randint(1, 20) for _ in range(10)}
B = {random.randint(1, 20) for _ in range(10)}
print("Giao của A và B:", A.intersection(B))
#8
A = {1, 2.5, "hello", 10, "python", 3.14}
int_count = len([x for x in A if type(x) == int])
float_count = len([x for x in A if type(x) == float])
str_count = len([x for x in A if type(x) == str])
print(f"Nguyên: {int_count}, Thực: {float_count}, Chuỗi: {str_count}")
#9 & 10
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
A = {i for i in range(1, m+1) if m % i == 0}
B = {i for i in range(1, n+1) if n % i == 0}
common_divisors = A & B
total_digit_sum = 0
for d in common_divisors:
    total_digit_sum += sum(int(digit) for digit in str(d))
print("Ước chung:", common_divisors)
print("Tổng chữ số của ước chung:", total_digit_sum)
#11
cpp = {1, 2, 3, 4, 5}
java = {4, 5, 6, 7}
python = {5, 8, 9}
both_3 = cpp & java & python
print("Sinh viên thi cả 3 ngôn ngữ:", both_3)
#12
n = int(input("Nhập n: "))
d = {i: i*i for i in range(1, n+1)}
print(d)
#13
W = input("Nhập chuỗi W: ")
char_count = {}
for char in W:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
#14
binary_dict = {i: bin(i)[2:] for i in range(1, 101)}
print(binary_dict)
#15
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)
#16
a = [1, 2, 3, 2, 4]
pairs = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + 1 == a[j]:
            pairs.append((i, j))
print("Các cặp chỉ số:", pairs)
#17
students = {}
while True:
    msv = input("Nhập MSV (6 ký tự, rỗng để dừng): ")
    if not msv: break
    name = input("Họ tên: ")
    score = float(input("Điểm: "))
    students[msv] = {'name': name, 'score': round(score)}
sorted_st = sorted(students.items(), key=lambda x: x[1]['score'], reverse=True)
print("Danh sách sau sắp xếp:", sorted_st)
#18
sbd_find = input("Nhập SBD cần tìm: ")
if sbd_find in students:
    print(f"Họ tên: {students[sbd_find]['name']}, Điểm: {students[sbd_find]['score']}")
else:
    print("Không tìm thấy thí sinh.")
#19
employees = {
    'NV01': {'name': 'Nguyen Van A', 'birth': 1990, 'salary': 5000000},
    'NV02': {'name': 'Tran Thi B', 'birth': 1995, 'salary': 7000000}
}
id_new = input("Mã NV mới: ")
name_new = input("Tên: ")
employees[id_new] = {'name': name_new, 'birth': 1992, 'salary': 6000000}
x = input("Nhập mã cần tìm: ")
print(employees.get(x, "Không thấy"))
y = input("Mã NV cần tăng lương: ")
if y in employees:
    employees[y]['salary'] += 1000000
z = input("Mã NV cần xóa: ")
employees.pop(z, None)
sorted_emp = sorted(employees.items(), key=lambda x: x[1]['birth'], reverse=True)
print("Danh sách sau sắp xếp:", sorted_emp)
