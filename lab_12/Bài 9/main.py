# bài 9:
from datetime import datetime

def tinh_tuan_trong_nam():
    try:
        # 1. Nhập liệu
        ngay_str = input("Nhập ngày (định dạng dd-mm-yyyy): ")
        
        # 2. Chuyển đổi chuỗi thành đối tượng date
        ngay = datetime.strptime(ngay_str, "%d-%m-%Y")
        
        # 3. Sử dụng isocalendar() để lấy thông tin tuần
        # isocalendar trả về tuple: (năm, tuần, thứ trong tuần)
        tuan = ngay.isocalendar()[1]
        
        print(f"Ngày {ngay_str} thuộc tuần thứ {tuan} của năm {ngay.year}.")
        
    except ValueError:
        print("Lỗi: Ngày bạn nhập không hợp lệ!")

# Chạy chương trình
if __name__ == "__main__":
    tinh_tuan_trong_nam()