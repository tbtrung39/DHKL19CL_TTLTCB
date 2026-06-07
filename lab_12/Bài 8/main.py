# Bài 8:
from datetime import datetime, timedelta

def tim_ngay_truoc_do():
    try:
        # 1. Nhập ngày
        ngay_str = input("Nhập ngày (định dạng dd-mm-yyyy): ")
        
        # 2. Chuyển chuỗi thành đối tượng datetime
        ngay_hien_tai = datetime.strptime(ngay_str, "%d-%m-%Y")
        
        # 3. Trừ đi 1 ngày (dùng timedelta)
        ngay_truoc_do = ngay_hien_tai - timedelta(days=1)
        
        # 4. In kết quả
        print(f"Ngày trước đó là: {ngay_truoc_do.strftime('%d-%m-%Y')}")
        
    except ValueError:
        print("Lỗi: Định dạng không đúng hoặc ngày không hợp lệ (ví dụ: ngày 30/02).")

# Chạy chương trình
if __name__ == "__main__":
    tim_ngay_truoc_do()