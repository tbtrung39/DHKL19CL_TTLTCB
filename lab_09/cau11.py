def gt_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * gt_kep(n-2)
n = int(input("Nhập n: "))
print(gt_kep(n))

def tong(k):
    if k == 1:
        return 1
    if k % 2 == 0:
        return tong(k-1) - gt_kep(k)
    else:
        return tong(k-1) + gt_kep(k)
k = int(input("Nhập k: "))
print(tong(k))