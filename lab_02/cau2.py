import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if a == 0:
    if b == 0:
        print("Vô nghiệm")
    else:
        print("x =", -c/b)
else:
    delta = b*b - 4*a*c
    print("delta", delta)
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        print("x =", -b/(2*a))
    else:
        print("x1 =", (-b + math.sqrt(delta))/(2*a))
        print("x2 =", (-b - math.sqrt(delta))/(2*a))