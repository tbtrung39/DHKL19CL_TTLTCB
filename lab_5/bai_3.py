n = int(input("Nhập số tự nhiên n: "))
if n == 0:
    print("Chuỗi nhị phân: 0")
else:
    nhi_phan = ""
    temp = n
    while temp > 0:
        nhi_phan = str(temp % 2) + nhi_phan
        temp //= 2
    print(f"Chuỗi nhị phân của {n} là: {nhi_phan}")