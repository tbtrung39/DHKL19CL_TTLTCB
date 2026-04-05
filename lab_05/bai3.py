n = int(input("Nhập số n: "))
kq = ""
while n > 0:
    kq = str(n % 2) + kq
    n //= 2
print("Nhị phân: ", kq)
