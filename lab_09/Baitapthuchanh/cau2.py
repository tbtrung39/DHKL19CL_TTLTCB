def ucln(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
a = input("Nhap a: ")
a=int(a)
b = input("Nhap b: ")
b=int(b)
t = ucln(a, b)
print("UCLN =", t)
# Giải thích:
# vd nhập a = 12, b = 15
# -> t = ucln(12, 15) -> 15 != 0 -> r = 12 % 15 = 12 -> a = 15 -> b = 12
# -> t = ucln(15, 12) -> 12 != 0 -> r = 15 % 12 = 3 -> a = 12 -> b = 3
# -> t = ucln(12, 3) -> 3 != 0 -> r = 12 % 3 = 0 -> a = 3 -> b = 0
# -> print("UCLN =", 3)