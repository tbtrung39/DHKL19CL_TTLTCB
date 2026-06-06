# Bài 8: 
def tinh_luong(he_so, chuc_vu):
    luong_co_ban = 1490000
    phu_cap = {"TP": 1000000, "PP": 700000, "NV": 300000}
    
    luong = he_so * luong_co_ban
    cap = phu_cap.get(chuc_vu, 0)
    thuc_linh = luong + cap
    return luong, cap, thuc_linh