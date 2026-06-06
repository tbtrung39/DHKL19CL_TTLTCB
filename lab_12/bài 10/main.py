# Bài 10:
from datetime import datetime

def tinh_khoang_cach_hai_ngay():
    try:
        # 1. Nhập liệu
        print("Nhập ngày thứ nhất:")
        ngay1_str = input("dd-mm-yyyy: ")
        print("Nhập ngày thứ hai:")
        ngay2_str = input("dd-mm-yyyy: ")
        
        # 2. Chuyển đổi thành đối tượng datetime
        d1 = datetime.strptime(ngay1_str, "%d-%m-%Y")
        d2 = datetime.strptime(ngay2_str, "%d-%m-%Y")
        
        # Đảm bảo d2 luôn lớn hơn d1 để tính toán
        if d1 > d2:
            d1, d2 = d2, d1
            
        # 3. Tính toán chênh lệch
        # Tính số năm
        nam = d2.year - d1.year
        # Điều chỉnh lại năm nếu chưa đến ngày sinh nhật trong năm của ngày thứ 2
        if (d2.month, d2.day) < (d1.month, d1.day):
            nam -= 1
            
        # Tính số tháng
        thang = d2.month - d1.month
        if d2.day < d1.day:
            thang -= 1
        if thang < 0:
            thang += 12
            
        # Tính số ngày
        # Lấy ngày của d2 trừ đi d1, nếu âm thì lấy số ngày của tháng trước đó cộng vào
        from calendar import monthrange
        if d2.day >= d1.day:
            ngay = d2.day - d1.day
        else:
            # Lấy ngày cuối cùng của tháng trước ngày d2
            thang_truoc = d2.month - 1 if d2.month > 1 else 12
            nam_truoc = d2.year if d2.month > 1 else d2.year - 1
            ngay_thang_truoc = monthrange(nam_truoc, thang_truoc)[1]
            ngay = ngay_thang_truoc - d1.day + d2.day
            
        print(f"\nKhoảng cách là: {nam} năm, {thang} tháng, {ngay} ngày.")
        
    except ValueError:
        print("Lỗi: Định dạng ngày không đúng hoặc ngày không tồn tại!")

# Chạy chương trình
if __name__ == "__main__":
    tinh_khoang_cach_hai_ngay()