import math
a = float(input('nhap a: '))
b= float(input('nhap b: '))
c= float(input('nhap c: '))
if a==0:
    print('khong phai pt bac 2')
else:
    d = b**b -4*a*c
    if d > 0: 
        print(f"x1={(-b+math.sqrt(d))/(2*a):.2f}, x2={(-b-math.sqrt(d))/(2*a):.2f}")
    elif d == 0: 
        print(f"x={-b/(2*a):.2f}")
    else: 
        print("Vo nghiem")