def tim_ucln(a, b):
    import math
    return math.gcd(a, b)
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f"UCLN của {a} và {b} là: {tim_ucln(a, b)}")