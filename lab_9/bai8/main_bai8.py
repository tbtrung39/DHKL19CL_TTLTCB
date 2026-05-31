import Matranvuong

mt, n = Matranvuong.nhap_ma_tran()

print("\nMa trận vừa nhập:")
Matranvuong.in_ma_tran(mt, n)

mt_cv = Matranvuong.ma_tran_chuyen_vi(mt, n)
print("\nMa trận chuyển vị:")
Matranvuong.in_ma_tran(mt_cv, n)

print(f"\nMa trận có đối xứng không? -> {Matranvuong.kiem_tra_doi_xung(mt, n)}")