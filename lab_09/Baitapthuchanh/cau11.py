def gt_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * gt_kep(n - 2)
k = input("Nhap k (<1000): ")
k = int(k)
S = 0
for i in range(1, k + 1):
    if i % 2 == 0:
        S = S - gt_kep(i)
    else:
        S = S + gt_kep(i)
print("S =", S)
# Giải thích:   
# vd nhập k = 5 -> gt_kep(1) - gt_kep(2) + gt_kep(3) - gt_kep(4) + gt_kep(5)
# -> 1 - 2 + 3 - 8 + 15
# -> return 9
# print("S =", 9)
