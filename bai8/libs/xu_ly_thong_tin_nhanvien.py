def tinh_phu_cap(chuc_vu):
    if chuc_vu == "TP":
        return 1_000_000
    elif chuc_vu == "PP":
        return 700_000
    else:
        return 300_000

def tinh_luong(he_so):
    return he_so * 1_490_000

def tinh_thuc_linh(luong, phu_cap):
    return luong + phu_cap

def nhap_nhan_vien():
    ma = input("Mã NV: ")
    ten = input("Tên NV: ")
    chuc_vu = input("Chức vụ (TP/PP/NV): ")
    he_so = float(input("Hệ số lương: "))
    luong = tinh_luong(he_so)
    phu_cap = tinh_phu_cap(chuc_vu)
    thuc_linh = tinh_thuc_linh(luong, phu_cap)
    return {
        "ma": ma, "ten": ten, "chuc_vu": chuc_vu,
        "he_so": he_so, "luong": luong,
        "phu_cap": phu_cap, "thuc_linh": thuc_linh
    }

def in_bang(ds):
    print(f"\n{'Mã':<8}{'Tên':<20}{'Chức vụ':<8}{'Hệ số':<8}{'Lương':<12}{'Phụ cấp':<12}{'Thực lĩnh'}")
    print("-" * 80)
    for nv in ds:
        print(f"{nv['ma']:<8}{nv['ten']:<20}{nv['chuc_vu']:<8}{nv['he_so']:<8}{nv['luong']:<12,.0f}{nv['phu_cap']:<12,.0f}{nv['thuc_linh']:,.0f}")