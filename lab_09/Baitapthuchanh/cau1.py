def so_lonnhat(a, b):
    if a > b:
        return a
    else:
        return b
x = input("Nhập số thứ nhất: ")
x = int(x)
y = input("Nhập số thứ hai: ")
y = int(y)
z = input("Nhập số thứ ba: ")
z = int(z)
m = so_lonnhat(x, y)
m = so_lonnhat(m, z)
print("Số lớn nhất là:", m)
# Giải thích:
# vd nhập x = 5, y = 10, z = 3
# -> m = so_lonnhat(5, 10) = 10
# -> m = so_lonnhat(10, 3) = 10
# -> print("Số lớn nhất là:", 10)
