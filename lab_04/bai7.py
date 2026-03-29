a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
x = a
y = b
while y != 0:
    r = x % y
    x = y
    y = r
ucln = x
bcnn = a * b // ucln
print(f"BCNN là: {bcnn}")