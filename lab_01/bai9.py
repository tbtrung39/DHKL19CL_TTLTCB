import math

x = float(input("Nhập x (x > 0, x != 1): "))

f_x = math.log(x, 4) + math.log(2, x)

print(f"Giá trị f({x}) = {round(f_x, 2)}")