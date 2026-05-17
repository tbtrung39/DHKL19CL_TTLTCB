import math
def can_trong(k):
    if k == 1:
        return (((2 + math.sqrt(1)))**(1/1)) ** (1/1)
    return ( k - 1 + (2 + math.sqrt(1))**(1/k))**(1/k)
def can_ngoai(n):
    if n == 1:
        return ( 1 + can_trong(1)) ** (1/(2))
    return ( n + can_trong(n)) ** (1/(n + 1))
n = input("Nhap n: ")
n = int(n)
S = can_ngoai(n)
print("S =", S)
# Giải thích:
# vd nhập n = 2 -> can_ngoai(2)
# -> (2 + can_trong(2)) ** (1/3)
# -> (2 + (1 + (2 + math.sqrt(1))**(1/2)) ** (1/2)) ** (1/3)
# -> return 1.5400882125049336
# print("S =", 1.5400882125049336)
