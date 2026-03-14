import math

x = float(input("Nhập x: "))

f = (-x + math.sqrt(x*x + 4)) / (7 * math.sqrt(x**4 + 1))

print("f(x) =", round(f, 2))