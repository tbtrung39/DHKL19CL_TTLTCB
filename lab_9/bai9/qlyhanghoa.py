def nhap_danh_sach_hang():
    ds_hang = []
    n = int(input("Nhập số lượng mặt hàng cần quản lý: "))
    for i in range(n):
        print(f"\n--- Nhập mặt hàng thứ {i+1} ---")
        ma = input("Mã hàng (4 ký tự): ")
        ten = input("Tên hàng: ")
        dvt = input("Đơn vị tính: ")
        gia = float(input("Đơn giá: "))
        sl = int(input("Số lượng: "))
        
        item = {
            'ma': ma, 'ten': ten, 'dvt': dvt, 
            'gia': gia, 'sl': sl, 'thanh_tien': 0.0, 'thue': 0.0
        }
        ds_hang.append(item)
    return ds_hang

def tinh_thanh_tien(ds_hang):
    for item in ds_hang:
        item['thanh_tien'] = item['gia'] * item['sl']

def tinh_thue(ds_hang):
    for item in ds_hang:
        item['thue'] = item['thanh_tien'] * 0.1

def hien_thi(ds_hang, tieu_de=""):
    print(f"\n===== {tieu_de} =====")
    print(f"{'Mã':<6}{'Tên hàng':<15}{'ĐVT':<8}{'Số lượng':<10}{'Đơn giá':<12}{'Thành tiền':<15}{'Thuế VAT':<12}")
    for item in ds_hang:
        print(f"{item['ma']:<6}{item['ten']:<15}{item['dvt']:<8}{item['sl']:<10}{item['gia']:<12,.0f}{item['thanh_tien']:<15,.0f}{item['thue']:<12,.0f}")

def sap_xep_giam_thue(ds_hang):
    return sorted(ds_hang, key=lambda x: x['thue'], reverse=True)