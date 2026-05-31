def tinh_tham_nien(nam_cong_tac):
    return nam_cong_tac * 500000 
def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    return luong_co_ban + tham_nien

def nhap_nhan_vien():
    ho_ten = input("Họ tên: ")
    que_quan = input("Quê quán: ")
    nam_ct = int(input("Số năm công tác: "))
    return ho_ten, que_quan, nam_ct

def xuat_nhan_vien(ho_ten, que_quan, nam_ct, luong):
    print("\n--- THÔNG TIN NHÂN VIÊN ---")
    print(f"Họ tên: {ho_ten} | Quê quán: {que_quan} | Thâm niên: {nam_ct} năm | Lương: {luong:,} VNĐ")

ten, que, nam = nhap_nhan_vien()
phu_cap_tn = tinh_tham_nien(nam)
tong_luong = tinh_luong(phu_cap_tn)
xuat_nhan_vien(ten, que, nam, tong_luong)