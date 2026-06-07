# bài 5
def ghep_phach():
    sbd_phach = {}
    with open('Sbd_Ph.dat', 'r') as f:
        for line in f:
            sbd, phach = line.split()
            sbd_phach[sbd] = phach

    sbd_ten = {}
    with open('Sbd_Ten.txt', 'r') as f:
        for line in f:
            parts = line.split(maxsplit=1) # Tách SBD và phần còn lại là tên
            sbd_ten[parts[0]] = parts[1].strip()

    phach_diem = {}
    with open('Phieu_Diem.txt', 'r') as f:
        for line in f:
            phach, diem = line.split()
            phach_diem[phach] = float(diem)

    danh_sach_thi_sinh = []
    for sbd, ten in sbd_ten.items():
        if sbd in sbd_phach:
            phach = sbd_phach[sbd]
            diem = phach_diem.get(phach, 0.0) # Lấy điểm, nếu không có thì trả về 0
            danh_sach_thi_sinh.append({
                'sbd': sbd,
                'ten': ten,
                'diem': diem
            })

    danh_sach_thi_sinh.sort(key=lambda x: x['diem'], reverse=True)

    with open('Ketqua.txt', 'w', encoding='utf-8') as f:
        f.write(f"{'SBD':<10} {'Họ tên':<20} {'Điểm':<5}\n")
        for ts in danh_sach_thi_sinh:
            f.write(f"{ts['sbd']:<10} {ts['ten']:<20} {ts['diem']:.2f}\n")
    
    print("Đã hoàn thành! Kết quả đã được ghi vào file Ketqua.txt.")

ghep_phach()