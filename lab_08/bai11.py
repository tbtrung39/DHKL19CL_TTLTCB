def nhap():
    ten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ten, toan, ly, hoa
def trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def xuat(ten, dtb):
    print("Họ tên:", ten)
    print("Điểm trung bình:", dtb)
ten, toan, ly, hoa = nhap()
dtb = trung_binh(toan, ly, hoa)
xuat(ten, dtb)