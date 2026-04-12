tong = 0
while True:
    s = input("Nhập (D/W số tiền): ")
    if s == "":
        break
    parts = s.split()
    if len(parts) != 2:
        print("Nhập sai format! Ví dụ: D 300")
        continue
    loai, tien = parts
    tien = int(tien)

    if loai == "D":
        tong += tien
    elif loai == "W":
        tong -= tien
print("Số dư:", tong)