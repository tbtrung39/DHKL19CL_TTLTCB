def uc(a, b):
    return a if b == 0 else uc(b, a % b)

def ucln(n):
    if len(n) == 1:
        return n[0]
    return uc(n[0], ucln(n[1:]))

lst = [int(x) for x in input("Nhập các số (cách nhau bằng dấu cách): ").split()]
print("Ước chung lớn nhất là:", ucln(lst))