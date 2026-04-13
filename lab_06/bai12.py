tong = 0
while True:
    s = input("Nhập (D/W số tiền, Enter để dừng): ")
    if s == "":
        break
    loai, tien = s.split()
    tien = int(tien)
    if loai == "D":
        tong = tong + tien
    elif loai == "W":
        tong = tong - tien
print("Số dư:", tong)