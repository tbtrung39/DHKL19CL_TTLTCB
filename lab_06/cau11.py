import random

n = int(input("Nhập n: "))
A = [int(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]
print("A:", A)

#1
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B:", B)

#2
C = [x**2 for x in A]
print("C:", C)

#3
chia_het_3 = [x for x in A if x % 3 == 0]
D = [random.choice(chia_het_3) for _ in range(len(chia_het_3))]
print("D:", D)