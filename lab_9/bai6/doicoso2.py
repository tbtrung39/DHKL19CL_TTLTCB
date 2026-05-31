def loai_bo_ky_tu_loi(chuoi):
    hop_le = "0123456789ABCDEF"
    chuoi_sach = "".join([c for c in chuoi.upper() if c in hop_le])
    return chuoi_sach

def doan_co_so(chuoi):
    hop_le = "0123456789ABCDEF"
    max_char = max(chuoi.upper())
    max_index = hop_le.index(max_char)
    
    if max_index >= 10: return 16
    if max_index >= 8: return 10
    if max_index >= 2: return 8
    return 2

def sang_co_so_10(chuoi, co_so_goc):
    try:
        return int(chuoi, co_so_goc)
    except ValueError:
        return "Chuỗi không hợp lệ với cơ số này!"