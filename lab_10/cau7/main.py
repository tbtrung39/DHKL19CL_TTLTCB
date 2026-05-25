import dayso
a = input("Nhap so luong phan tu: ")
a = int(a)
ds = dayso.sinh_day_so(a)
dayso.hien_thi(ds)
dayso.snt_chia_het_7(ds)
print("Tong cac so le trong day:", dayso.tong_so_le(ds))
dayso.liet_ke_scp(ds)