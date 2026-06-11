import string

ALPHANUMERIC = set(string.ascii_letters + string.digits)
danh_sach_email = []

print("Nhập danh sách username (Gõ 'exit' hoặc để trống để dừng):")
while True:
    try:
        username = input("Nhap username: ").strip()
        if username.lower() == 'exit' or username == '':
            break
            
        if " " in username:
            raise ValueError("Lỗi: Username không được chứa khoảng trắng!")
            
        if not all(char in ALPHANUMERIC for char in username):
            raise ValueError("Lỗi: Username chỉ được bao gồm chữ số (0-9), chữ cái thường (a-z) và hoa (A-Z)!")
            
        email_hoan_chinh = username + "@companyname.com"
        danh_sach_email.append(email_hoan_chinh)
        print(f"-> Đã thêm thành công: {email_hoan_chinh}")
        
    except ValueError as e:
        print(e)

print(f"\nDanh sách Email công ty đã lưu: {danh_sach_email}")