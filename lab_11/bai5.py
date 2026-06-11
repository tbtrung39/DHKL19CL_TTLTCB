def bai_5():
    try:
        sbd_to_phach = {}
        with open('Sbd_Phah.dat', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    sbd_to_phach[parts[0]] = parts[1]
                    
    
        sbd_to_ten = {}
        with open('SBD_Ten.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(maxsplit=1)
                if len(parts) >= 2:
                    sbd_to_ten[parts[0]] = parts[1]
                    
       
        phach_to_diem = {}
        with open('Phieu_Diem.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    phach_to_diem[parts[0]] = float(parts[1])
                    
       
        danh_sach_ts = []
        for sbd, ten in sbd_to_ten.items():
            phach = sbd_to_phach.get(sbd)
            if phach and phach in phach_to_diem:
                diem = phach_to_diem[phach]
                danh_sach_ts.append({
                    'sbd': sbd,
                    'hoten': ten,
                    'diem': diem
                })
                
       
        danh_sach_ts.sort(key=lambda x: x['diem'], reverse=True)
        

        with open('Ketqua.txt', 'w', encoding='utf-8') as f_out:
            for ts in danh_sach_ts:
                f_out.write(f"{ts['sbd']}\t{ts['hoten']}\t{ts['diem']}\n")
                
        print("Đã lắp ráp dữ liệu và ghi vào file 'Ketqua.txt' thành công.")
        
    except FileNotFoundError as e:
        print(f"Lỗi: Thiếu file dữ liệu đầu vào. Chi tiết: {e}")
