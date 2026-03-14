# Bài 1:
import math
a, b, c = map(float, input("Nhập a, b, c (cách nhau khoảng trắng): ").split())
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm" if c == 0 else "Phương trình vô nghiệm")
    else:
        print(f"Phương trình bậc 1 có nghiệm x = {-c/b:.2f}")
else:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print(f"Phương trình có nghiệm kép x = {-b/(2*a):.2f}")
    else:
        can_delta = math.sqrt(delta)
        x1 = (-b + can_delta) / (2*a)
        x2 = (-b - can_delta) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")