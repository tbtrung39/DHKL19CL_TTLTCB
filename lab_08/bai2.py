def ucln(a,b):
    while b != 0:
        a, b = b, a % b
    return a
tu = int(input("Nhập tử sô: "))
mau = int(input("Nhập mẫu số: "))
g = ucln(tu, mau)
print(f"Phân số rút gọn: {tu // g}/{mau // g}")
