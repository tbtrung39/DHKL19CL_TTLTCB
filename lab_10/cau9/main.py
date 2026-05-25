import quanlyhanghoa
ds = []
n = input("Nhap so mat hang: ")
n = int(n)
for i in range(n):
    print("Nhap mat hang thu", i + 1)
    hang = quanlyhanghoa.nhap_hang()
    ds.append(hang)
print("Danh sach mat hang:")
quanlyhanghoa.xuat(ds)
quanlyhanghoa.sap_xep(ds)
print("Danh sach mat hang sau khi sap xep:")
quanlyhanghoa.xuat(ds)