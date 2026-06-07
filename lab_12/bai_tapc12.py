#Bài 2
def ktra_nhap():
    chuoi_trc=""
    while True:
        try:
            s=input("nhập 1 chuỗi ký tự :")
            if s in ["a","b","z","A","B","Z"]:
                print("Đã nhập ký tự kthuc hoạt động bth")
                break
            if not s.isprintable() or s == "":
                raise Exception("Lỗi ký tự !")
            for i in range(len(s) - 1):
                if s[i] == s[i+1]:
                    raise Exception("Lỗi nhập liệu !")
            if "####" in s:  
                raise Exception("Lỗi nhập lặp lại !")
            if s== chuoi_trc:
                raise Exception ("Lỗi trùng lặp !")    
            chuoi_trc=s
            print("Nhập thành công ",s)
        except Exception as e:
            print("Xử lí ngoại lệ",e)
ktra_nhap()

#Bài 4
import os
def sao_chep_tap_tin_kieu_moi(ten_file_nguon, ten_file_dich="copy.dat"):    
    try:
        if not os.path.exists(ten_file_nguon):
            raise FileNotFoundError(f"Tập tin {ten_file_nguon} không tìm thấy")
        with open(ten_file_nguon, "r", encoding="utf-8") as f_doc:
            noi_dung = f_doc.read()
            print("Đã đọc xong dữ liệu từ file:", ten_file_nguon)
        with open(ten_file_dich, "w", encoding="utf-8") as f_ghi:
            f_ghi.write(noi_dung)
            print("Đã ghi xong dữ liệu vào file: ",ten_file_dich)
        print("Sao chép tập tin hoàn tất và thành công!")
    except FileNotFoundError as e:
        print("Lỗi ",e)
    except PermissionError:
        print("ko có quyền truy cập")
    except Exception as e:
        print("Lỗi ",e)
sao_chep_tap_tin_kieu_moi("tailieu.txt")

#Bài 6
def tao_email():
    while True:
        try:
            ten=input("Nhập tên nhân viên :").strip()
            if not ten:
                print("ctrinh dừng")
                break
            if not ten.isalnum():
                raise ValueError("Tên nhân viên không được có dấu cách, dấu tiếng Việt hoặc ký tự đặc biệt!")
            email = ten + "@companyname.com"
            print("Email được tạo thành công: ",email)    
        except ValueError as e:
            print("lỗi",e)
tao_email()

#Bài 8
from datetime import datetime, timedelta
def tim_ngay_hom_truoc():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        ngay_hien_tai = datetime(nam, thang, ngay)
        ngay_hom_truoc = ngay_hien_tai - timedelta(days=1)
        print(f"Ngày hôm trước của ngày đã nhập là: {ngay_hom_truoc.strftime('%d-%m-%Y')}")     
    except ValueError:
        print("Lỗi Ngày, tháng hoặc năm nhập vào không hợp lệ!")
tim_ngay_hom_truoc()

#Bài 10
from datetime import datetime

def tinh_khoang_cach_ngay():
    dinh_dang = "%d-%m-%Y"
    try:
        chuoi_ngay1 = input("Nhập ngày thứ nhất : ").strip()
        chuoi_ngay2 = input("Nhập ngày thứ hai : ").strip()
        dt1 = datetime.strptime(chuoi_ngay1, dinh_dang)
        dt2 = datetime.strptime(chuoi_ngay2, dinh_dang)
        tong_so_ngay = abs((dt2 - dt1).days)
        print(f"\nTổng số ngày chênh lệch: {tong_so_ngay} ngày")
        nam = tong_so_ngay // 365
        ngay_con_lai = tong_so_ngay % 365
        thang = ngay_con_lai // 30
        ngay = ngay_con_lai % 30
        print(f" Quy đổi: 2 ngày này cách nhau khoảng {nam} năm, {thang} tháng, {ngay} ngày.")
    except ValueError:
        print("Lỗi Sai định dạng chuỗi nhập vào! Vui lòng nhập đúng mẫu dd-mm-yyyy.")
tinh_khoang_cach_ngay()