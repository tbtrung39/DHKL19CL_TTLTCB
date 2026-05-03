import random
n = input("Nhập n: ")
n = int(n)
A = set()
while len(A) < n:
    x = round(random.uniform(-100, 100), 2)
    A.add(x)
print("Tập hợp A:", A)
print("Phần tử nhỏ nhất: ", min(A))
print("Phần tử lớn nhất: ", max(A))
print("Tổng các phần tử: ", sum(A))