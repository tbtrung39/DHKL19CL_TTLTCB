a = input("Nhập a: ")
a = int(a)
b = input("Nhập b: ")
b = int(b)
x = a
y = b
while y != 0:
    r = x % y
    x = y
    y = r
ucln = x
bcnn = (a * b) // ucln
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)
