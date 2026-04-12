tong = 0
while True:
    s = input()
    if not s:
        break
    loai, tien = s.split()
    tien = int(tien)
    if loai == "D":
        tong += tien
    elif loai == "W":
        tong -= tien
print("Số dư: ", tong)