n = int(input("Nhập n: "))
dem = 0
so = 2
while dem < n:
    nt = True
    for i in range(2, so):
        if so % i == 0:
            nt = False
    if nt == True:
        print(so)
        dem = dem + 1
    so = so + 1
    