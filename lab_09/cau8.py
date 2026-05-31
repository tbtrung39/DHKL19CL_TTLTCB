# Câu a:
def tong(n):
    if n == 1:
        return 1/(1*2)
    return tong(n-1) + 1/(n*(n+1))
n = int(input("Nhập n: "))
print(tong(n))

# Câu b:
def gt(n):
    if n == 0 or n == 1:
        return 1
    return n * gt(n-1)
def tong(n):
    if n == 1:
        return 1
    return tong(n-1) + 1/gt(n)
n = int(input("Nhập n: "))
print(tong(n))

# Câu c:
import math
def tinh(i, n):
    if i == n:
        return math.sqrt(3*n)
    return math.sqrt(3*i + tinh(i+1, n))
n = int(input("Nhập n: "))
print(tinh(1, n))

# Câu d:
def tinh(i):
    if i == 1:
        return 1
    return (i - 1 + tinh(i-1)) ** (1/i)
n = int(input("Nhập n: "))
print((n + tinh(n)) ** (1/(n+1)))