def tinh_X(n):
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        tong = tong + (n - i)**2 * tinh_X(i)
    return tong
n = input("Nhap n: ")
n = int(n)
kq = tinh_X(n)
print("X =", kq)
# Giải thích:
# vd nhập n = 3 -> tinh_X(3)
# -> (3 - 0)**2 * tinh_X(0) + (3 - 1)**2 * tinh_X(1) + (3 - 2)**2 * tinh_X(2)
# -> 9 * 1 + 4 * 1 + 1 * 5
# -> return 18
# print("X =", 18)