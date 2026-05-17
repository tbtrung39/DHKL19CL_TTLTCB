def ucln(a,b):
    while b != 0:
        du = a % b
        a = b
        b = du
    return a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN = ", ucln(a,b))