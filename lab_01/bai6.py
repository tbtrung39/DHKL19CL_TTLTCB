import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm" if c != 0 else "Phương trình vô số nghiệm")
    else:
        print(f"Phương trình có 1 nghiệm x = {round(-c/b, 2)}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép x = {round(x, 2)}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")