n = int(input("Nhập số sinh viên: "))
sv = {}
for i in range(n):
    ma = input("Mã sinh viên: ")
    ten = input("Tên sinh viên: ")
    diem = float(input("Điểm: "))
    diem = round(diem)
    sv[ma] = {
        "ten": ten,
        "diem": diem
    }
ds = sorted(sv.items(), key=lambda x: x[1]["diem"], reverse=True)
print("\nDanh sách sinh viên:")
for ma, thongtin in ds:
    print(ma, "-", thongtin["ten"], "-", thongtin["diem"])