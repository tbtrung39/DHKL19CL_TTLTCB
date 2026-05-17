def tinh_x(n):
    if n == 0:
        return 1
    
    tong = 0
    for i in range(n):
        tong += ((n - i) ** 2) * tinh_x(i)
    return tong

n = int(input())
print(tinh_x(n))