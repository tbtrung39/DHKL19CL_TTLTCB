def la_so_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = input("Nhap vao n: ")
n = int(n)
ds = []
for i in range(n):
    x = input(f"Nhap phan tu thu {i + 1}: ")
    x = int(x)
    ds.append(x)
tong = 0
for i in ds:
    if la_so_chan(i):
        tong = tong + i
print("Danh sach:", ds)
print("Tong cac so chan:", tong)