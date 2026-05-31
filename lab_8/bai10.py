def in_uoc_so(n):
    uoc_so = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc_so.append(i)
    return uoc_so
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    print(f"Các ước của {n} là: {in_uoc_so(n)}")