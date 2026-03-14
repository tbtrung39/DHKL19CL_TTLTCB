import math
x = float(input("Nhập x: "))
fx = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x))
print(f"Giá trị f(x) = {round(fx, 2)}")