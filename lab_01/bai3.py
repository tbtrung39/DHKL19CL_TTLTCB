import math
x = float(input("Nhap x: "))
f = (-x + math.sqrt(x**2 + 4)) / ((x**4 + 1)**(1/7))
print("Gia tri F(x) = ", round(f,2))