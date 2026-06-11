import math

def Ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def Bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // Ucln(a, b)

def SumDivisor(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong