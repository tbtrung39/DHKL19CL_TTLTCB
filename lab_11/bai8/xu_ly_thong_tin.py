import csv
import os

def tinh_luong_va_phu_cap(nv):
    he_so = float(nv.get('He_so_luong', 0))
    luong = he_so * 1490000
    
    chuc_vu = nv.get('Chuc_vu', '').strip().upper()
    if chuc_vu == 'TP':
        phu_cap = 1000000
    elif chuc_vu == 'PP':
        phu_cap = 700000
    elif chuc_vu == 'NV':
        phu_cap = 300000
    else:
        phu_cap = 0
        
    thuc_linh = luong + phu_cap
    
    nv['Luong'] = luong
    nv['Phu_cap'] = phu_cap
    nv['Thuc_linh'] = thuc_linh
    return nv

def luu_file_csv(danh_sach, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    headers = ['Ma_NV', 'Ten_NV', 'Chuc_vu', 'He_so_luong', 'Luong', 'Phu_cap', 'Thuc_linh']
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for nv in danh_sach:
            writer.writerow(nv)