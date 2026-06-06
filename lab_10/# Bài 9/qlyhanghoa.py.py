# Bài 9: 
def nhap_danh_sach_hang_hoa(n):
    danh_sach = []
    for i in range(n):
        print(f"\nNhập thông tin mặt hàng thứ {i+1}:")
        ma = input("Mã hàng: ")
        ten = input("Tên hàng: ")
        dvt = input("Đơn vị tính: ")
        gia = float(input("Đơn giá: "))
        sl = int(input("Số lượng: "))
        
        thanh_tien = gia * sl
        thue = thanh_tien * 0.1
        
        hang_hoa = {
            "ma": ma, "ten": ten, "dvt": dvt, 
            "gia": gia, "sl": sl, 
            "thanh_tien": thanh_tien, "thue": thue
        }
        danh_sach.append(hang_hoa)
    return danh_sach

def hien_thi(danh_sach):
    print(f"\n{'Mã':<10} {'Tên':<15} {'Thành tiền':<15} {'Thuế':<10}")
    for item in danh_sach:
        print(f"{item['ma']:<10} {item['ten']:<15} {item['thanh_tien']:<15} {item['thue']:<10}")

def sap_xep_giam_dan_theo_thue(danh_sach):
    # Sắp xếp danh sách dựa trên giá trị 'thue', reverse=True là giảm dần
    danh_sach.sort(key=lambda x: x['thue'], reverse=True)
    return danh_sach