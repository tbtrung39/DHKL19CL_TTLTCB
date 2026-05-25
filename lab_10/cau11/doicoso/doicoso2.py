def loc_ky_tu(s):
    hop_le = "0123456789ABCDEF"
    kq = ""
    s = s.upper()
    for ky_tu in s:
        if ky_tu in hop_le:
            kq = kq + ky_tu
    return kq
def kiem_tra(s):
    s = s.upper()
    dung = True
    for c in s:
        if c not in "01":
            dung = False
            break
    if dung:
        return 2
    
    dung = True
    for c in s:
        if c not in "01234567":
            dung = False
            break
    if dung:
        return 8
    
    dung = True
    for c in s:
        if c not in "0123456789":
            dung = False
            break
    if dung:
        return 10
    
    dung = True
    for c in s:
        if c not in "0123456789ABCDEF":
            dung = False
            break
    if dung:
        return 16
    
def sang_he_10(s, co_so):
    he16 = "0123456789ABCDEF"
    s = s.upper()
    tong = 0
    mu = 0
    for i in range(len(s)-1, -1, -1):
        gia_tri = he16.index(s[i])
        tong = tong + gia_tri * (co_so ** mu)
        mu = mu + 1
    return tong
    