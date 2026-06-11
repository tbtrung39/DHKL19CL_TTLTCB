from datetime import datetime, timedelta

def nhap_ngay_hop_le():
    while True:
        try:
            chuoi_ngay = input("Nhap ngay theo dinh dang (dd-mm-yyyy): ")
            ngay_dt = datetime.strptime(chuoi_ngay, "%d-%m-%y") if len(chuoi_ngay.split('-')[-1]) == 2 else datetime.strptime(chuoi_ngay, "%d-%m-%Y")
            return ngay_dt
        except ValueError:
            print("Định dạng ngày không hợp lệ hoặc ngày không tồn tại. Vui lòng nhập lại!")

# --- BÀI 7: Tìm ngày kế tiếp ---
print("--- BÀI 7: TÌM NGÀY KẾ TIẾP ---")
ngay_hien_tai = nhap_ngay_hop_le()
ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
print(f"-> Ngày kế tiếp là: {ngay_ke_tiep.strftime('%d-%m-%Y')}\n")

# --- BÀI 8: Tìm ngày trước đó ---
print("--- BÀI 8: TÌM NGÀY TRƯỚC ĐÓ ---")
ngay_goc = nhap_ngay_hop_le()
ngay_truoc = ngay_goc - timedelta(days=1)
print(f"-> Ngày trước đó là: {ngay_truoc.strftime('%d-%m-%Y')}\n")

# --- BÀI 9: Ngày đó thuộc tuần thứ mấy trong năm ---
print("--- BÀI 9: XÁC ĐỊNH TUẦN THỨ MẤY ---")
ngay_kiem_tra = nhap_ngay_hop_le()
# %V trả về số thứ tự tuần theo chuẩn ISO 8601
so_tuan = ngay_kiem_tra.strftime("%V")
print(f"-> Ngày này thuộc tuần thứ: {so_tuan} trong năm.\n")

# --- BÀI 10: Khoảng cách giữa 2 ngày (Năm, tháng, ngày) ---
print("--- BÀI 10: KHOẢNG CÁCH GIỮA 2 NGÀY ---")
print("Nhập ngày thứ nhất:")
date1 = nhap_ngay_hop_le()
print("Nhập ngày thứ hai:")
date2 = nhap_ngay_hop_le()

khoang_cach = abs(date2 - date1)
tong_so_ngay = khoang_cach.days

nam = tong_so_ngay // 365
ngay_du = tong_so_ngay % 365
thang = ngay_du // 30
ngay = ngay_du % 30

print(f"-> Hai ngày cách nhau khoảng: {nam} năm, {thang} tháng, và {ngay} ngày (Tổng cộng {tong_so_ngay} ngày).")