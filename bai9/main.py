with open(r"bai9\PASSENGERS.IN", "r") as f:
    lines = f.readlines()

n = int(lines[0].strip())

trong_luong_tung_hanh_khach = []
for i in range(1, 1 + n):
    cac_tui = list(map(float, lines[i].strip().split()))
    trong_luong_tung_hanh_khach.append(cac_tui)

tong_trong_luong = []
so_tui = []
for i in range(n):
    tong = 0
    for tui in trong_luong_tung_hanh_khach[i]:
        tong = tong + tui
    tong_trong_luong.append(tong)
    so_tui.append(len(trong_luong_tung_hanh_khach[i]))

with open(r"bai9\WEIGHT.OUT", "w") as f:
    for tong in tong_trong_luong:
        f.write("{:.2f}\n".format(tong))

danh_sach_huy = []
for i in range(n):
    if tong_trong_luong[i] > 23 or so_tui[i] > 5:
        danh_sach_huy.append(i + 1)  # số thứ tự bắt đầu từ 1

with open(r"bai9\CANCELED.OUT", "w") as f:
    for stt in danh_sach_huy:
        tong = tong_trong_luong[stt - 1]
        so = so_tui[stt - 1]
        if tong > 23:
            f.write("{} -> So thu tu cua khach co tong trong luong do xach tay vuot qua 23 kg".format(stt))
        if so > 5:
            f.write("{} -> So thu tu cua hanh khach co so luong do xach tay vuot qua 05".format(stt))

print("Danh sach hanh khach bi huy chuyen bay:")
for stt in danh_sach_huy:
    tong = tong_trong_luong[stt - 1]
    so = so_tui[stt - 1]
    print("Hanh khach thu {}: tong trong luong = {:.2f} kg, so tui = {}".format(stt, tong, so))
    if tong > 23:
        print("  -> Vi pham: tong trong luong vuot qua 23 kg")
    if so > 5:
        print("  -> Vi pham: so luong tui vuot qua 5")