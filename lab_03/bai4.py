n = input("Nhập n:")
n = int(n)
for x in range(2, n + 1):
    la_so_nguyen_to = True
    for i in range(2, x):
        if x % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(x, "là số nguyên tố nhỏ hơn hoặc bằng", n)