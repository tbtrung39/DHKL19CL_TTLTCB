def quay_lui_hoan_vi(hoan_vi_hien_tai, da_xet, n):
    if len(hoan_vi_hien_tai) == n:
        print(hoan_vi_hien_tai)
        return

    for so in range(1, n + 1):
        if not da_xet[so]:
            da_xet[so] = True 
            quay_lui_hoan_vi(hoan_vi_hien_tai + [so], da_xet, n)
            da_xet[so] = False 

n = int(input("Nhập số tự nhiên n: "))
da_xet = [False] * (n + 1)

print(f"Các hoán vị của dãy từ 1 đến {n} là:")
quay_lui_hoan_vi([], da_xet, n)