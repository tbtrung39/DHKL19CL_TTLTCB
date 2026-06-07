# Bài 7:
def tim_so_chung(file1, file2, file_ket_qua):
    try:
        with open(file1, 'r') as f1:
            set1 = set(map(int, f1.read().split()))
            
        with open(file2, 'r') as f2:
            set2 = set(map(int, f2.read().split()))
            
        so_chung = set1.intersection(set2)
        
        with open(file_ket_qua, 'w') as f_out:
            if so_chung:
                f_out.write(" ".join(map(str, sorted(so_chung))))
                print(f"Đã tìm thấy {len(so_chung)} số chung. Kết quả đã lưu tại {file_ket_qua}")
            else:
                f_out.write("Không có số chung.")
                print("Không tìm thấy số chung nào.")
                
        with open(file_ket_qua, 'r') as f_read:
            print(f"Nội dung file {file_ket_qua}: {f_read.read()}")
            
    except FileNotFoundError as e:
        print(f"Lỗi: {e}")
    except ValueError:
        print("Lỗi: File chứa dữ liệu không phải là số nguyên.")

tim_so_chung('m_nums.txt', 'n_nums.txt', 'so_chung.txt')