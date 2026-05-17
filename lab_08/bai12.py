def nhap():
    ho_ten = input("Nhap ho ten: ")
    que_quan = input("Nhap que quan: ")
    tham_nien = input("Nhap tham nien cong tac (nam): ")
    tham_nien = int(tham_nien)
    return ho_ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    if tham_nien < 1:
        return 5000000
    elif tham_nien <= 3:
        return 7000000
    else:
        return 10000000
def xuat(ho_ten, que_quan, tham_nien, luong):
    print("Ho ten:", ho_ten)
    print("Que quan:", que_quan)
    print(f"Tham nien cong tac: {tham_nien} nam")
    print("Luong:", luong)
ho_ten, que_quan, tham_nien = nhap()
luong = tinh_luong(tham_nien)
xuat(ho_ten, que_quan, tham_nien, luong)