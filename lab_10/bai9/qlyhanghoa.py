def nhap_danh_sach_hang():
    ds_hang = []
    n = int(input("Nhap so luong mat hang can them: "))
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        while True:
            ma = input("Ma hang (chuoi 4 ky tu): ")
            if len(ma) == 4: break
            print("Ma hang bat buoc phai co dung 4 ky tu!")
            
        ten = input("Ten hang: ")
        dvt = input("Don vi tinh: ")
        don_gia = float(input("Don gia: "))
        so_luong = int(input("So luong: "))
        
        item = {
            'ma': ma, 'ten': ten, 'dvt': dvt, 
            'don_gia': don_gia, 'so_luong': so_luong,
            'thanh_tien': 0.0, 'thue_VAT': 0.0
        }
        ds_hang.append(item)
    return ds_hang

def tinh_thanh_tien_va_vat(ds_hang):
    for item in ds_hang:
        item['thanh_tien'] = item['don_gia'] * item['so_luong']
        item['thue_VAT'] = item['thanh_tien'] * 0.10

def in_danh_sach(ds_hang, tieu_de=""):
    print(f"\n--- {tieu_de} ---")
    print(f"{'Ma':<6} | {'Ten hang':<15} | {'DVT':<6} | {'Don gia':<10} | {'SL':<5} | {'Thanh tien':<12} | {'Thue VAT':<10}")
    print("-" * 80)
    for item in ds_hang:
        print(f"{item['ma']:<6} | {item['ten']:<15} | {item['dvt']:<6} | {item['don_gia']:<10:g} | {item['so_luong']:<5} | {item['thanh_tien']:<12:g} | {item['thue_VAT']:<10:g}")

def sap_xep_giam_dan_theo_thue(ds_hang):
    return sorted(ds_hang, key=lambda x: x['thue_VAT'], reverse=True)