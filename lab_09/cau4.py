def hoan_vi(ds,start):
    if start == len(ds):
        print(ds)
        return
    for i in range(start, len(ds)):
        ds[start], ds[i] = ds[i], ds[start]
        hoan_vi(ds, start + 1)
        ds[start], ds[i] = ds[i], ds[start]
n = int(input("Nhập n: "))
ds = []
for i in range(1, n + 1):
    ds.append(i)
hoan_vi(ds, 0)
