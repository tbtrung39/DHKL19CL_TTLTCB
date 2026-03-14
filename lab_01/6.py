import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b*b - 4*a*c
print("delta =", delta)
if delta < 0:
    print("Phương trình vô nghiệm")

elif delta == 0:
    x = -b/(2*a)
    print("Nghiệm kép x=", round(x,2))

else:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print("x1 =", round(x1,2))
    print("x2 =", round(x2,2))
