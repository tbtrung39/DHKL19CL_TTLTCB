def nhap():
    ten = input("Nhập họ tên: ")
    que = input("Nhập quê quán: ")
    nam = int(input("Nhập thâm niên công tác: "))
    return ten, que, nam
def tinh_luong(nam):
    return nam * 1000000
def xuat(ten, que, nam, luong):
    print("Họ tên:", ten)
    print("Quê quán:", que)
    print("Thâm niên:", nam)
    print("Lương:", luong)
ten, que, nam = nhap()
luong = tinh_luong(nam)
xuat(ten, que, nam, luong)