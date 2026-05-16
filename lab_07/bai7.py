import random
n = int(input("Nhập số phần tử của A: "))
m = int(input("Nhập số phần tử của B: "))
kytu ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOQPRSTUVWXYZ0123456789"
A = set()
B = set()
while len(A) < n:
    A.add(random.choice(kytu))
while len(B) < m:
    B.add(random.choice(kytu))
print("Tập hợp A: ", A)
print("Tập hợp B: ", B)
print("Các phần tử chung: ", A&B)
