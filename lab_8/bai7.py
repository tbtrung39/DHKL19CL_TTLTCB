def tim_min_max(a, b, c):
    so_nho_nhat = min(a, b, c)
    so_lon_nhat = max(a, b, c)
    return so_nho_nhat, so_lon_nhat
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))

nho, lon = tim_min_max(x, y, z)
print(f"Số nhỏ nhất là: {nho}")
print(f"Số lớn nhất là: {lon}")