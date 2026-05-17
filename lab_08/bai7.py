def lon_nhat(a, b, c):
    return max(a, b, c)
def nho_nhat(a, b, c):
    return min(a, b, c)
a = int(input("Nhập số thứ 1: "))
b = int(input("Nhập số thứ 2: "))
c = int(input("Nhập số thứ 3: "))
print("Số lớn nhất: ", lon_nhat(a, b, c))
print("Số nhỏ nhất: ", nho_nhat(a, b, c))