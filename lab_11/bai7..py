def bai_7():
    try:
        with open('m_nums.txt', 'r', encoding='utf-8') as f:
            set_m = set(f.read().split())
            
        with open('n_nums.txt', 'r', encoding='utf-8') as f:
            set_n = set(f.read().split())
            
        so_chung = set_m.intersection(set_n)
        
        with open('so_chung.txt', 'w', encoding='utf-8') as f_out:
            f_out.write(" ".join(so_chung))
            
        print("Các số có mặt ở cả 2 file văn bản là:")
        print(" ".join(so_chung))
        
    except FileNotFoundError as e:
        print(f"Lỗi: Thiếu file cấu thành. Chi tiết: {e}")

