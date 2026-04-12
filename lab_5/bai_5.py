s = input("Nhập chuỗi: ")
so_str = "".join([c for c in s if c.isdigit()])

if so_str:
    n = int(so_str)
    print(f"Số trích xuất được: {n}")
    
    # Kiểm tra số hoàn hảo
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    
    if tong_uoc == n and n != 0:
        print(f"{n} là số hoàn hảo.")
    else:
        print(f"{n} không phải là số hoàn hảo.")
else:
    print("Không tìm thấy số trong chuỗi.")