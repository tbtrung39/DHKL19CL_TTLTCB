def loc_chuoi(chuoi):
    tap_hop = "0123456789ABCDEF"
    chuoi_loc = "".join([c for c in chuoi.upper() if c in tap_hop])
    print(f"Chuoi sau khi loc: {chuoi_loc}")
    return chuoi_loc

def doan_co_so(chuoi):
    chuoi = chuoi.upper()
    co_the_la_bin = all(c in "01" for c in chuoi)
    co_the_la_oct = all(c in "01234567" for c in chuoi)
    co_the_la_dec = all(c in "0123456789" for c in chuoi)
    
    if co_the_la_bin:
        return "Co the la bieu dien cua co so: 2, 8, 10, 16"
    elif co_the_la_oct:
        return "Co the la bieu dien cua co so: 8, 10, 16"
    elif co_the_la_dec:
        return "Co the la bieu dien cua co so: 10, 16"
    else:
        return "Bieu dien cua co so: 16"

def nhi_phan_sang_thap_phan(chuoi):
    return int(chuoi, 2)

def bat_phan_sang_thap_phan(chuoi):
    return int(chuoi, 8)

def thap_luc_sang_thap_phan(chuoi):
    return int(chuoi, 16)