import math

def rut_gon_phan_so(tu_so, mau_so):
    ucln = math.gcd(tu_so, mau_so)
    tu_moi = tu_so // ucln
    mau_moi = mau_so // ucln
    return tu_moi, mau_moi
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
if mau == 0:
    print("Mẫu số phải khác 0!")
else:
    t_moi, m_moi = rut_gon_phan_so(tu, mau)
    print(f"Phân số sau khi rút gọn: {t_moi}/{m_moi}")