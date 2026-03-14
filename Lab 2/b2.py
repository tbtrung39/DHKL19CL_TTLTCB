'''Nhập vào hệ số a, b, c và tìm ra nghiệm của hệ ptrinh bậc 2'''
import math
a , b , c = map(float, input("Nhập 3 số:  ").split())
delta = b*b - (4*a*c)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Nghiệm của phương trình là x1: ", x1)
    print(f"Nghiệm của phương trình là x2: ", x2) 
elif delta == 0:
    print ("Phương trình có nghiệm kép x: ", x = -b / (2*a))
else:
    print("Phương trình vô nghiệm")