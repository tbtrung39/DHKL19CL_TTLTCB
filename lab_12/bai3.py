ten_file = input("Nhap ten tap tin can doc: ")

try:
    with open(ten_file, "r", encoding="utf-8") as f_goc:
        noi_dung = f_goc.read()
        
    with open("copy.dat", "w", encoding="utf-8") as f_copy:
        f_copy.write(noi_dung)
        
    print("-> Đã đọc và sao chép thành công nội dung vào tập tin 'copy.dat'")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tập tin nào có tên '{ten_file}'. Chương trình kết thúc.")