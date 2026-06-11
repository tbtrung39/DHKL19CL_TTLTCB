import string
KY_TU_HOP_LE = set(string.ascii_letters)

while True:
    try:
        chuoi = input("Nhap mot chuoi ky tu (Nhan Enter de thoat): ")
        if chuoi == "": 
            break
            
        for ky_tu in chuoi:
            if ky_tu not in KY_TU_HOP_LE:
                raise ValueError("Lỗi ký tự !!!")
                
        if any(chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3] == chuoi[i+4] for i in range(len(chuoi) - 4)):
            raise ValueError("Lỗi nhập trùng lặp!!!")
            
        if any(chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3] for i in range(len(chuoi) - 3)):
            raise ValueError("Lỗi nhập lặp lại !!!")
            
        if any(chuoi[i] == chuoi[i+1] for i in range(len(chuoi) - 1)):
            raise ValueError("Lỗi nhập liệu !!!")
            
        print("-> Chuỗi hợp lệ, việc nhập liệu kết thúc bình thường.")
        
    except ValueError as e:
        print(e)
        print("Chương trình tiếp tục hoạt động bình thường...\n")