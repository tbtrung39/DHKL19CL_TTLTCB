sbd_phach = {}
with open(r"bai5/Sbd_ph.dat", "r") as f:
    for line in f:
        parts = line.split()
        sbd, sophach = int(parts[0]), int(parts[1])
        sbd_phach[sbd] = sophach

sbd_ten = {}
with open(r"bai5/SBD_Ten.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(None, 1)  # tách tối đa 2 phần
        sbd, hoten = int(parts[0]), parts[1]
        sbd_ten[sbd] = hoten

phach_diem = {}
with open(r"bai5\Phiem_Diem.txt", "r") as f:
    for line in f:
        parts = line.split()
        sophach, diem = int(parts[0]), int(parts[1])
        phach_diem[sophach] = diem

# Lắp ráp thông tin: sbd -> hoten, diem
danh_sach = []
for sbd in sbd_phach:
    sophach = sbd_phach[sbd]
    hoten = sbd_ten.get(sbd, "Không rõ")
    diem = phach_diem.get(sophach, 0)
    danh_sach.append((sbd, hoten, diem))

# Sắp xếp theo điểm giảm dần
danh_sach.sort(key=lambda x: x[2], reverse=True)

# Ghi ra Ketqua.txt
with open(r"bai5\Ketqua.txt", "w", encoding="utf-8") as f:
    for sbd, hoten, diem in danh_sach:
        f.write(f"{sbd} {hoten} {diem}\n")
        print(f"{sbd} | {hoten} | {diem}")

print("done")