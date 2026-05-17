#a
def tinh_tong_a(n):
    if n == 1:
        return 1 / (1 * 2)
    return 1 / (n * (n + 1)) + tinh_tong_a(n - 1)

n = int(input())
print(tinh_tong_a(n))

#b
def tinh_giai_thua(k):
    if k == 0 or k == 1:
        return 1
    return k * tinh_giai_thua(k - 1)

def tinh_tong_b(n):
    if n == 1:
        return 1 / tinh_giai_thua(1)
    return 1 / tinh_giai_thua(n) + tinh_tong_b(n - 1)

n = int(input())
print(tinh_tong_b(n))

#c
import math

def tinh_can_c(n, hien_tai=1):
    if hien_tai == n:
        return math.sqrt(3 * n)
    return math.sqrt(3 * hien_tai + tinh_can_c(n, hien_tai + 1))

n = int(input())
print(tinh_can_c(n))

#d
def tinh_can_d(n, hien_tai=1):
    if hien_tai == n:
        return (n + 1) ** (1 / (n + 1))
    return (hien_tai + tinh_can_d(n, hien_tai + 1)) ** (1 / (hien_tai + 1))

n = int(input())
print(tinh_can_d(n))