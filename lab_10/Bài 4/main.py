# bài 4:
def lay_cac_uoc_nguyen_to(n):
    uoc_nt = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            uoc_nt.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        uoc_nt.append(temp)
    return uoc_nt

def xu_ly_uoc_nguyen_to(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            data = f_in.read().split()
            numbers = [int(x) for x in data]
        
        with open(output_file, 'w') as f_out:
            for num in numbers:
                if num < 2:
                    f_out.write("Không có ước nguyên tố\n")
                else:
                    uoc = lay_cac_uoc_nguyen_to(num)
                    # Ghi các ước nguyên tố cách nhau bởi dấu cách trên cùng 1 dòng
                    f_out.write(" ".join(map(str, uoc)) + "\n")
                    
        print(f"Đã xử lý xong. Kiểm tra kết quả tại {output_file}")
        
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file input.")

xu_ly_uoc_nguyen_to('f_in.dat', 'f_out.dat')