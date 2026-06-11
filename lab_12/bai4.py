ten_file_doc = input("Nhap ten file can doc: ")
ten_file_ghi = input("Nhap ten file muon ghi (sinh vien tu dat): ")

f_doc = None
f_ghi = None

try:
    f_doc = open(ten_file_doc, "r", encoding="utf-8")
    noi_dung = f_doc.read()
    
    f_ghi = open(ten_file_ghi, "w", encoding="utf-8")
    f_ghi.write(noi_dung)
    print("-> Thao tác tệp tin hoàn tất thành công.")

except FileNotFoundError:
    print("Thông báo: Tập tin nguồn để đọc không tồn tại!")
except IOError:
    print("Thông báo: Lỗi vào/ra dữ liệu (Mở sai chế độ hoặc không có quyền ghi/đọc file)!")
except Exception as e:
    print(f"Thông báo lỗi hệ thống: {e}")
finally:
    if f_doc and not f_doc.closed:
        f_doc.close()
        print("Đã đóng file đọc.")
    if f_ghi and not f_ghi.closed:
        f_ghi.close()
        print("Đã đóng file ghi.")