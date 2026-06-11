import Matranvuong

mt, n = Matranvuong.nhap_ma_tran()
Matranvuong.in_ma_tran(mt, n)

mt_cv = Matranvuong.ma_tran_chuyen_vi(mt, n)
print("Ma tran chuyen vi:")
Matranvuong.in_ma_tran(mt_cv, n)

if Matranvuong.kiem_tra_doi_xung(mt, n):
    print("Ket qua: True (Ma tran doi xung)")
else:
    print("Ket qua: False (Ma tran khong doi xung)")