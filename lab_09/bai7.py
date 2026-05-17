def quay_lui_tim_nghiem(tong_con_lai, so_luong_con_lai, gia_tri_truoc, nghiem_hien_tai):
    if so_luong_con_lai == 0:
        if tong_con_lai == 0:
            print(" + ".join(map(str, nghiem_hien_tai)))
        return

    if tong_con_lai < 0:
        return

    for so_chon in range(gia_tri_truoc, tong_con_lai + 1):
        quay_lui_tim_nghiem(
            tong_con_lai - so_chon,
            so_luong_con_lai - 1,
            so_chon,
            nghiem_hien_tai + [so_chon]
        )

N = int(input())
n = int(input())
quay_lui_tim_nghiem(N, n, 1, [])