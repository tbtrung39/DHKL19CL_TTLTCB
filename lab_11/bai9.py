def bai_9():
    try:
        with open('PASSENGERS.IN', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        if not lines:
            return
            
        so_khach = int(lines[0].strip())
        hanh_khach_data = []
        
        idx = 1
        for i in range(so_khach):
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            if idx < len(lines):
                weights = [float(w) for w in lines[idx].strip().split()]
                hanh_khach_data.append(weights)
                idx += 1

        weight_out_data = []
        canceled_out_data = []

        for index, weights in enumerate(hanh_khach_data, start=1):
            tong_trong_luong = sum(weights)
            so_luong_kien = len(weights)
            
            weight_out_data.append(f"{tong_trong_luong:.2f}")
            
            if tong_trong_luong > 23.0:
                canceled_out_data.append(f"{index} -> Số thứ tự của khách có tổng trọng lượng đồ xách tay vượt quá 23 kg.")
            elif so_luong_kien > 5:
                canceled_out_data.append(f"{index} -> Số thứ tự của hành khách có số lượng đồ xách tay vượt quá 05.")

        with open('WEIGHT.OUT', 'w', encoding='utf-8') as f_weight:
            for w in weight_out_data:
                f_weight.write(w + "\n")
                
        with open('CANCELED.OUT', 'w', encoding='utf-8') as f_canceled:
            for item in canceled_out_data:
                f_canceled.write(item + "\n")
                
        print("--- THÔNG BÁO HÀNH KHÁCH BỊ HỦY CHUYẾN ---")
        if canceled_out_data:
            for item in canceled_out_data:
                print(item)
        else:
            print("Không có hành khách nào bị hủy chuyến.")
            
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file dữ liệu đầu vào PASSENGERS.IN")

