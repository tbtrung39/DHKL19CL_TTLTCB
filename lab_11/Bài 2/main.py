# Bài 2:
def sap_xep_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            du_lieu = f.read()
            ds_so = [int(x) for x in du_lieu.split()]
       
        ds_so.sort()
        
        with open(output_file, 'w') as f:
            # Chuyển các số thành chuỗi và nối lại bằng dấu cách
            ket_qua = " ".join(map(str, ds_so))
            f.write(ket_qua)
            
        print(f"Đã sắp xếp xong. Dữ liệu đã được lưu vào {output_file}")
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {input_file}")
    except ValueError:
        print("Lỗi: Dữ liệu trong file không phải là số hợp lệ.")

sap_xep_file('f_in.dat', 'f_out.dat')