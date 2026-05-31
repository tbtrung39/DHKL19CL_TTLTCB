def ucln(a,b):
    if b == 0:
        return a
    return ucln(b, a % b)
n = int(input("Nhập n: "))
kq = 0
for i in range(n):
    x = int(input("Nhập số: "))
    if i == 0:
        kq = x
    else:
        kq = ucln(kq,x)
print("UCLN là: ", kq)

