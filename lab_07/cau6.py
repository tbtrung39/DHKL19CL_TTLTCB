n = input("Nhập n: ")
n = int(n)
dem = 0
so = 2
while dem < n:
    la_snt = True
    i = 2
    while i <= so // 2:
        if so % i == 0:
            la_snt = False
        i = i + 1
    if la_snt:
        print(so,end=" ")
        dem = dem + 1
    so = so + 1
    