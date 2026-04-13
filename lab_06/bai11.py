n = input("Nhập n: ")
n = int(n)
A = list(map(int, input("Nhập A: ").split()))

#a 
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B:",B)
#b
C = [x**2 for x in A]
print("C:",C)
#c
import random
D = [x for x in A if x % 3 == 0]
D = random.sample(D, min(3, len(D)))
print("D:", D)