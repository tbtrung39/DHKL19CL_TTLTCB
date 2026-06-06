# Bài 3:
def tim_cuc_tri(input_file, output_file):
    try:
        # 1. Đọc dữ liệu từ file
        with open(input_file, 'r') as f:
            ds_so = [int(x) for x in f.read().split()]
            
        if len(ds_so) < 3:
            print("Dãy số quá ngắn, không thể tìm cực trị.")
            return

        # 2. Tìm các điểm cực trị
        cuc_tri = []
        # Duyệt từ phần tử thứ 2 đến áp chót
        for k in range(1, len(ds_so) - 1):
            if (ds_so[k-1] < ds_so[k] > ds_so[k+1]) or (ds_so[k-1] > ds_so[k] < ds_so[k+1]):
                cuc_tri.append(ds_so[k])

        # 3. Ghi ra file f_out.dat theo yêu cầu
        with open(output_file, 'w') as f:
            # Dòng 1: Số lượng các giá trị cực trị
            f.write(f"{len(cuc_tri)}\n")
            # Dòng 2: Danh sách các giá trị cực trị
            f.write(" ".join(map(str, cuc_tri)))
            
        print(f"Đã tìm thấy {len(cuc_tri)} điểm cực trị. Kết quả đã lưu vào '{output_file}'.")

    except FileNotFoundError:
        print(f"Không tìm thấy file '{input_file}'.")

# Chạy chương trình
tim_cuc_tri('f_in.dat', 'f_out.dat')