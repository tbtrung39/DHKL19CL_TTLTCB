import csv

def nhap_danh_sach_sv():
    ds = []
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nNhập thông tin sinh viên thứ {i+1}:")
        ma_sv = input("Mã SV: ")
        ho_ten = input("Họ tên: ")
        diem_tb = float(input("Điểm TB: "))
        diem_rl = float(input("Điểm RL (rèn luyện): "))
        
        sv = {
            'ma_sv': ma_sv,
            'ho_ten': ho_ten,
            'diem_tb': diem_tb,
            'diem_rl': diem_rl,
            'diem_tl': 0.0
        }
        ds.append(sv)
    return ds

def tinh_diem_tl(ds):
    for sv in ds:
        sv['diem_tl'] = (sv['diem_tb'] + sv['diem_rl']) / 2
    return ds

def in_va_luu_danh_sach(ds, file_path='files/ds_sinhvien.csv'):
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    print(f"\n{'Mã SV':<12}{'Họ và tên':<25}{'Điểm TB':<10}{'Điểm RL':<10}{'Điểm TL':<10}")
    print("-" * 67)
    for sv in ds:
        print(f"{sv['ma_sv']:<12}{sv['ho_ten']:<25}{sv['diem_tb']:<10.2f}{sv['diem_rl']:<10.2f}{sv['diem_tl']:<10.2f}")
        
    headers = ['ma_sv', 'ho_ten', 'diem_tb', 'diem_rl', 'diem_tl']
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(ds)
    print(f"\n-> Đã lưu danh sách vào {file_path}")

def sap_xep_tang_dan_diem_rl(ds):
    return sorted(ds, key=lambda x: x['diem_rl'])

def in_sinh_vien_max_diem_tl(ds):
    if not ds:
        print("Danh sách rỗng.")
        return
    max_diem = max(sv['diem_tl'] for sv in ds)
    print(f"\n--- Sinh viên có điểm TL cao nhất ({max_diem:.2f}) ---")
    for sv in ds:
        if sv['diem_tl'] == max_diem:
            print(f"Mã SV: {sv['ma_sv']} | Họ tên: {sv['ho_ten']} | Điểm TL: {sv['diem_tl']:.2f}")