def ucln(a,b):
    while b != 0:
        du = a % b
        a = b
        b = du
    return a
def bcnn(a,b):
    return a * b // ucln(a,b)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN là: ", bcnn(a,b))
