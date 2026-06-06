# bai 7:
from datetime import datetime, timedelta

def tim_ngay_ke_tiep():
    try:
        # 1. Nhập liệu
        ngay_str = input("Nhập ngày (định dạng dd-mm-yyyy): ")
        
        # 2. Chuyển chuỗi thành đối tượng datetime
        ngay_hien_tai = datetime.strptime(ngay_str, "%d-%m-%Y")
        
        # 3. Cộng thêm 1 ngày
        ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
        
        # 4. In kết quả
        print(f"Ngày kế tiếp là: {ngay_ke_tiep.strftime('%d-%m-%Y')}")
        
    except ValueError:
        print("Lỗi: Định dạng ngày không đúng (phải là dd-mm-yyyy) hoặc ngày không tồn tại!")

# Chạy chương trình
if __name__ == "__main__":
    tim_ngay_ke_tiep()