a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Tìm Ước chung lớn nhất (UCLN) trước
x, y = a, b
while y != 0:
    x, y = y, x % y
ucln = x

# BCNN = (a * b) / UCLN
bcnn = abs(a * b) // ucln
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")