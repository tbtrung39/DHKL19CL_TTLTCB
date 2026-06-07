from lab_10.Bai6.doicoso2 import *

def main():
    chuoikytu = input("Nhập một chuỗi ký tự: ")
    print("Chuỗi đã lọc: ",loc_chuoikytu(chuoikytu))
    chuoi_loc = loc_chuoikytu(chuoikytu)
    print("Hệ cơ số: ",detect_hecoso(chuoi_loc))
    print("Giá trị thập phân (nếu applicable): ")
    print(convert_binary_to_decimal(chuoi_loc))
    print(convert_octal_to_decimal(chuoi_loc))
    print(convert_hexadecimal_to_decimal(chuoi_loc))

if __name__ == "__main__":
    main()