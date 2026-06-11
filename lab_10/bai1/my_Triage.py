import math

def is_TamGiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def ChuViTamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        return a + b + c
    return 0

def S_TamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        p = ChuViTamGiac(a, b, c) / 2

        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    return 0