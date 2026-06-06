# Bài 1: 
def tinh_tong_so_le(ten_file):
    try:
        # Mở file để đọc
        with open(ten_file, 'r') as f:
            # Đọc toàn bộ nội dung file
            du_lieu = f.read()
            # Tách các số dựa trên khoảng trắng và chuyển sang kiểu int
            danh_sach_so = [int(x) for x in du_lieu.split()]
            
            # Tính tổng các số lẻ (số % 2 != 0)
            tong_le = sum(so for so in danh_sach_so if so % 2 != 0)
            
            return tong_le
    except FileNotFoundError:
        return "Không tìm thấy file!"
    except ValueError:
        return "Dữ liệu trong file không hợp lệ (không phải số nguyên)!"

# Thực thi
ket_qua = tinh_tong_so_le('dayso.dat')
print(f"Tổng các số hạng lẻ trong file là: {ket_qua}")