import math
a = float(input("Nhap a = "))
b = float(input("Nhap b = "))
c = float(input("Nhap c = "))
delta = b**b - 4*a*c
if delta < 0:
   print("Phuong trinh vo nghiem")
elif delta == 0:
    x = -b/(2*a)
    print("Phuong trinh co nghiem kep = ",round(x,2))
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phuong trinh co nghiem x1 = ", round(x1,2))
    print("Phuong trinh co nghiem x2 = ", round(x2,2))