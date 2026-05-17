def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
def S(n):
    if n == 1:
        return 1 
    S_moi = S(n - 1) + 1 / giai_thua(n)
    return S_moi
n = input("Nhap n: ")
n = int(n)
S = S(n)
print("S =", S)
# Giải thích:
# vd nhập n = 3 -> S(3)
# -> S(2) + 1/giai_thua(3)
# -> S(1) + 1/giai_thua(2) + 1/giai_thua(3)
# -> 1 + 1/2 + 1/6
# -> return 5/3
# print("S =", 5/3)