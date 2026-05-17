def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)

def tinh_tong_s(k):
    tong = 0
    for i in range(1, k + 1):
        dau = (-1) ** (i + 1)
        tong += dau * giai_thua_kep(i)
    return tong

k = int(input())
print(tinh_tong_s(k))