import math
def tong_can(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3*n + tong_can(n - 1))
n = input("Nhap n: ")
n = int(n)
kq = tong_can(n)
print("Tong can:", kq)
# Giải thích:
# vd nhập n = 3 -> tong_can(3)
# -> math.sqrt(3*3 + tong_can(2))
# -> math.sqrt(9 + math.sqrt(3*2 + tong_can(1)))
# -> math.sqrt(9 + math.sqrt(6 + math.sqrt(3)))
# -> return 3.4322961035638673
# print("Tong can:", 3.4322961035638673)