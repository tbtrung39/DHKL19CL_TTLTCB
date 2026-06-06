# Bài 1:
def tinh_tong_so_le(ten_file):
    try:
        # 1. Mở file để đọc
        with open(ten_file, 'r') as f:
            # 2. Đọc nội dung, tách thành danh sách các số (dùng split để xử lý cả khoảng trắng/xuống dòng)
            du_lieu = f.read().split()
            danh_sach_so = [int(x) for x in du_lieu]
            
            # 3. Tính tổng các số lẻ (số chia 2 dư khác 0)
            tong_le = sum(so for so in danh_sach_so if so % 2 != 0)
            
            return tong_le
    except FileNotFoundError:
        return "Lỗi: Không tìm thấy file 'dayso.dat'."
    except ValueError:
        return "Lỗi: File chứa ký tự không phải là số."

# Gọi hàm và in kết quả
ket_qua = tinh_tong_so_le('dayso.dat')
print(f"Tổng các số hạng lẻ trong file là: {ket_qua}")


