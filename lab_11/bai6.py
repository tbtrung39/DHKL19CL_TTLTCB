def bai_6():
    ma_tran_mau = (
        "4\n"
        "211 133 180 5\n"
        "192 168 1 254\n"
        "11 1 11 233\n"
    )
    with open('matrix.txt', 'w', encoding='utf-8') as f:
        f.write(ma_tran_mau)
        
    print("--- Thực hiện yêu cầu bài 6 ---")
    try:
        with open('matrix.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
        print("a. Nội dung dòng đầu tiên:")
        print(lines[0])
        if len(lines) >= 3:
            print("a. Nội dung dòng thứ 3:")
            print(lines[2])
            
        print("\nb. Nội dung toàn bộ file:")
        for line in lines:
            print(line)
            
        print("\nc. Đang lọc số lẻ và tạo file ODD.txt...")
        
        matrix_data = []
        for line in lines[1:]: 
            row = [int(x) for x in line.split()]
            matrix_data.append(row)
            
        odd_matrix = []
        for row in matrix_data:
            new_row = []
            for num in row:
                if num % 2 != 0:
                    new_row.append(str(num))
                else:
                    new_row.append('0')
            odd_matrix.append(new_row)
            
        with open('ODD.txt', 'w', encoding='utf-8') as f_odd:
            for row in odd_matrix:
                f_odd.write(" ".join(row) + "\n")
                

        print("d. Nội dung dòng cuối của file ODD.txt:")
        if odd_matrix:
            print(" ".join(odd_matrix[-1]))
            
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file matrix.txt")
