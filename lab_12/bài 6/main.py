# bài 6:
def nhap_danh_sach_email():
    ds_email = []
    
    while True:
        try:
            username = input("Nhập username (hoặc gõ 'exit' để dừng): ")
            if username.lower() == 'exit':
                break
                
            # Kiểm tra xem username có rỗng không
            if not username:
                raise ValueError("Username không được để trống!")
                
            # Kiểm tra tính hợp lệ: chỉ chứa chữ cái và chữ số
            # isalnum() trả về True nếu tất cả ký tự là chữ hoặc số
            if not username.isalnum():
                raise ValueError("Username chỉ được chứa chữ cái và chữ số!")
            
            # Ghép thành email và lưu vào danh sách
            email = f"{username}@companyname.com"
            ds_email.append(email)
            print(f"Đã thêm: {email}")
            
        except ValueError as e:
            print(f"Lỗi nhập liệu: {e}")
            
    return ds_email

# Chạy chương trình
danh_sach = nhap_danh_sach_email()
print("\nDanh sách email đã nhập:")
print(danh_sach)