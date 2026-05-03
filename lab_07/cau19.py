A = {}
#a
n = input("Nhap so nhan vien: ")
n = int(n)
i = 0
while i < n:
    ma = input("Nhap ma nhan vien (4 ky tu so): ")
    ten = input("Nhap ho ten: ")
    ns = input("Nhap nam sinh: ")
    ns = int(ns)
    luong = input("Nhap luong: ")
    luong = int(luong)
    A[ma] = {
        "ten": ten,
        "ns": ns,
        "luong": luong
    }
    i = i + 1
#b
print("Them nhan vien moi:")
ma = input("Nhap ma nhan vien (4 ky tu so): ")
ten = input("Nhap ho ten: ")
ns = input("Nhap nam sinh: ")
ns = int(ns)
luong = input("Nhap luong: ")
luong = int(luong)
A[ma] = {
    "ten": ten,
    "ns": ns,
    "luong": luong
}
#c
x = input("Nhap ma nhan vien can tim: ")
if x in A:
    print("Thong tin nhan vien:", A[x])
else:
    print("Khong tim thay nhan vien.")
#d
y = input('Nhap ma nhan vien can tang luong: ')
if y in A:
    A[y]["luong"] = A[y]["luong"] + 1000000
    print("Da tang luong.", A[y])
else:
    print("Khong tim thay nhan vien.")
#e
z = input("Nhap ma nhan vien can xoa: ")
if z in A:
    del A[z]
    print("Da xoa nhan vien.")
else:
    print("Khong tim thay nhan vien.")
#f
print("Danh sach nhan vien giam dan theo nam sinh:")
ds = list(A.items())
i = 0
while i < len(ds) - 1:
    j = i + 1
    while j < len(ds):
        if ds[i][1]["ns"] < ds[j][1]["ns"]:
            k = ds[i]
            ds[i] = ds[j]
            ds[j] = k
        j = j + 1
    i = i + 1
for i in ds:
    print(i)