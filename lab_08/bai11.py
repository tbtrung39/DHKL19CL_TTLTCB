def nhap():
    ho_ten = input("Nhap ho ten: ")
    toan = input("Nhap diem toan: ")
    toan = float(toan)
    ly = input("Nhap diem ly: ")
    ly = float(ly)
    hoa = input("Nhap diem hoa: ")
    hoa = float(hoa)
    return ho_ten, toan, ly, hoa
def diem_trung_binh(toan, ly, hoa):
    dtb = (toan + ly + hoa) / 3
    return dtb
def xuat(ho_ten,dtb):
    print("Ho ten:", ho_ten)
    print("Điem trung binh:", dtb)
ho_ten, toan, ly, hoa = nhap()
dtb = diem_trung_binh(toan, ly, hoa)
xuat(ho_ten, dtb)