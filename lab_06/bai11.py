import random

n = int(input("Nhập n: "))
A = [int(input()) for i in range(n)]
print("A =", A)

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B =", B)

C = [x**2 for x in A]
print("C =", C)

D = [x for x in A if x % 3 == 0]
if len(D) > 0:
    print("D (random):", random.choice(D))
else:
    print("Không có số thỏa mãn")