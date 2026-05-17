def permutation(n):
    if n == 1:
        return [[1]]
    
    hoan_vi_truoc = permutation(n - 1)
    ket_qua_moi = []
    
    for mien in hoan_vi_truoc:
        for vi_tri in range(len(mien) + 1):
            hoan_vi_moi = mien[:vi_tri] + [n] + mien[vi_tri:]
            ket_qua_moi.append(hoan_vi_moi)
            
    return ket_qua_moi

n = int(input("Nhập số tự nhiên n: "))
danh_sach_hoan_vi = permutation(n)

print(f"Hàm trả về danh sách gồm {len(danh_sach_hoan_vi)} phần tử:")
print(danh_sach_hoan_vi)