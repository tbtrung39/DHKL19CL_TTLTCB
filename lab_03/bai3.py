n = input("Nhập n: ")
n = int(n)
la_so_nguyen_to = True
if n < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break

if la_so_nguyen_to:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

    nho_hon = n - 1
    while nho_hon >= 2:
        check = True
        for i in range(2, nho_hon):
            if nho_hon % i == 0:
                check = False
                break
        if check:
            break
        else:
            nho_hon = nho_hon - 1

    lon_hon = n + 1
    while True:
        check = True
        for i in range(2, lon_hon):
            if lon_hon % i == 0:
                check = False
                break
        if check:
            break
        else:
            lon_hon = lon_hon + 1

    if n - nho_hon < lon_hon - n:
        print("Số nguyên tố gần nhất với", n, "là", nho_hon)
    else:
        print("Số nguyên tố gần nhất với", n, "là", lon_hon)




    