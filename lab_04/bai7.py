# Tìm bội chung nhỏ nhất của hai số nguyên dương a và b.
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

so_a = a
so_b = b
while b != 0:
    so_du = a % b
    print(so_du)
    a = b
    b = so_du                       

BCNN = (so_a * so_b) // a
print("Bội chung nhỏ nhất của", so_a, "và", so_b, "là:", BCNN)

# Thuật toán Euclid (Euclidean Algorithm)
#Thuật toán Euclid: Tìm UCLN bằng cách chia lấy dư liên tục a % b
# Công thức liên hệ: Sau khi có UCLN, ta dùng công thức:
# BCNN(a, b) = (a * b) / UCLN(a, b)
