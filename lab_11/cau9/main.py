with open("PASSENGER.IN", "r") as file:
    n = int(file.readline())
    ds_tong = []
    ds_huy = []
    for i in range(n):
        line = file.readline().split()
        weights = list(map(float, line))
        tong = sum(weights)
        so_mon = len(weights)
        ds_tong.append(tong)
        ly_do = ""
        if tong > 23:
            ly_do = ly_do + "Tong trong luong vuot qua 23kg. "
        if so_mon > 5:
            ly_do = ly_do + "So luong do xach tay vuot qua 5."

        if ly_do != "":
            ds_huy.append((i + 1, tong, so_mon, ly_do))
with open("WEIGHT.OUT", "w") as file:
    for tong in ds_tong:
        file.write("{:.2f}\n".format(tong))
with open("CANCELED.OUT", "w") as file:
    for hk in ds_huy:
        file.write(
            "Hanh khach thu {} - Tong: {:.2f}kg - So mon: {} - {}\n".format(
                hk[0],
                hk[1],
                hk[2],
                hk[3]
            )
        )
print("DANH SACH HANH KHACH BI HUY CHUYEN:\n")
if len(ds_huy) == 0:
    print("Khong co hanh khach nao bi huy chuyen.")
else:
    for hk in ds_huy:
        print("Hanh khach thu:", hk[0])
        print("Tong trong luong:", "{:.2f}".format(hk[1]), "kg")
        print("So luong do:", hk[2])
        print("Ly do:", hk[3])
       