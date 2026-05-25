import matranvuong
n = input("Nhap cap ma tran: ")
n = int(n)
a = matranvuong.nhap_ma_tran(n)
print("Ma tran:")
matranvuong.xuat_ma_tran(a)
print("Ma tran chuyen vi:")
b = matranvuong.chuyen_vi(a)
matranvuong.xuat_ma_tran(b)
if matranvuong.doi_xung(a):
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")