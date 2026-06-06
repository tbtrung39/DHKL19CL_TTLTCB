# bài 2:
def sap_xep_file(input_file, output_file):
    try:
        # 1. Đọc dữ liệu từ file f_in.dat
        with open(input_file, 'r') as f:
            # f.read() đọc toàn bộ nội dung, split() tách các số theo khoảng trắng
            du_lieu = f.read().split()
            # Chuyển đổi các chuỗi thành số nguyên
            ds_so = [int(x) for x in du_lieu]
        
        # 2. Sắp xếp danh sách tăng dần
        ds_so.sort()
        
        # 3. Ghi kết quả vào file f_out.dat
        with open(output_file, 'w') as f:
            # Chuyển các số thành chuỗi và nối lại bằng dấu cách
            ket_qua = " ".join(map(str, ds_so))
            f.write(ket_qua)
            
        print(f"Đã sắp xếp thành công! Dữ liệu đã được lưu vào '{output_file}'.")
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{input_file}'.")
    except ValueError:
        print("Lỗi: Dữ liệu trong file không phải là số hợp lệ.")

# Chạy chương trình
sap_xep_file('f_in.dat', 'f_out.dat')