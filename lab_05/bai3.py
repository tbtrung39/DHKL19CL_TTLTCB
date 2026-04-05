n = int(input("Nhập số n: "))
if n == 0:
    print("Dạng nhị phân: 0")
else:
    ket_qua = ""
    while n > 0:
        du = n % 2
        ket_qua = str(du) + ket_qua
        n = n // 2  
    print("Dạng nhị phân:", ket_qua)
