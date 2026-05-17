def reduce(ham, ds):
    kq = ds[0]
    for i in range(1, len(ds)):
        kq = ham(kq, ds[i])
    return kq
n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)
so_chan = list(filter(lambda x: x % 2 == 0, a))
tong = reduce(lambda x, y: x + y, so_chan)
print("Danh sách:", a)
print("Các số chẵn:", so_chan)
print("Tổng số chẵn =", tong)