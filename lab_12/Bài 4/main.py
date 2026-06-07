# bài 4:
def lay_cac_uoc_nguyen_to(n):
    """Hàm tìm các ước nguyên tố khác nhau của n"""
    uoc_nt = set()
    d = 2
    temp = n
    # Phân tích thừa số nguyên tố
    while d * d <= temp:
        while temp % d == 0:
            uoc_nt.add(d) # Thêm ước nguyên tố vào tập hợp (set tự loại bỏ trùng lặp)
            temp //= d
        d += 1
    if temp > 1:
        uoc_nt.add(temp)
    return sorted(list(uoc_nt))

def xu_ly_uoc_nguyen_to(input_file, output_file):
    try:
        # 1. Đọc dữ liệu từ f_in.dat
        with open(input_file, 'r') as f_in:
            data = f_in.read().split()
            numbers = [int(x) for x in data]
        
        # 2. Ghi ước nguyên tố vào f_out.dat
        with open(output_file, 'w') as f_out:
            for num in numbers:
                if num < 2:
                    f_out.write("Không có ước nguyên tố\n")
                else:
                    uoc = lay_cac_uoc_nguyen_to(num)
                    # Ghi các ước nguyên tố cách nhau bởi dấu cách trên cùng 1 dòng
                    f_out.write(" ".join(map(str, uoc)) + "\n")
                    
        print(f"Đã xử lý xong. Kiểm tra kết quả tại '{output_file}'")
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{input_file}'.")
    except ValueError:
        print("Lỗi: Dữ liệu trong file không phải là số hợp lệ.")

# Chạy chương trình
xu_ly_uoc_nguyen_to('f_in.dat', 'f_out.dat')