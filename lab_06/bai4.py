# Nhập danh sách
ds = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    ds.append(x)
print("Danh sách ban đầu:", ds)
chen = [1, 2, 3]
ds = chen + ds
ds = ds + chen
if len(ds) >= 4:
    ds = ds[:4] + chen + ds[4:]

print("Sau khi chèn:", ds)


k = int(input("Nhập vị trí k cần xóa: "))

if 0 <= k < len(ds):
    ds.pop(k)
else:
    print("Vị trí không hợp lệ")

print("Sau khi xóa:", ds)

print("Tăng dần:", sorted(ds))
print("Giảm dần:", sorted(ds, reverse=True))