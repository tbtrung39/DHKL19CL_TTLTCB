def premutation(ds):
    if len(ds) == 1:
        return [ds]
    kq = []
    for i in range(len(ds)):
        x = ds[i]
        con_lai = ds[:i] + ds[i+1:]
        for p in premutation(con_lai):
            kq.append([x] + p)
    return kq
n = int(input("Nhập n: "))
ds = []
for i in range(1, n + 1):
    ds.append(i)
print(premutation(ds))