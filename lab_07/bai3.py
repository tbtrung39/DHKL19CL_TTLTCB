import random
n = int(input("Nhập n: "))
A = set()
while len(A) < n:
    x = round(random.uniform(0,100), 2)
    A.add(x)
print("Tập hợp A: ", A)
print("Phần tử nhỏ nhất: ", min(A))
print("Phần tử lớn nhất: ", max(A))
print("Tổng các phần tử: ", sum(A))
