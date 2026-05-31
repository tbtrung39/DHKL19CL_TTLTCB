import math

def tim_bcnn(a, b):
    # BCNN(a, b) = (a * b) / UCLN(a, b)
    return abs(a * b) // math.gcd(a, b)
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f"BCNN của {a} và {b} là: {tim_bcnn(a, b)}")