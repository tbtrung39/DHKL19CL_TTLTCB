so = int(input("Nhập số nguyên dương: "))
tam = so
for i in range(2, so + 1):
    dem = 0  
    for j in range(2, tam + 1):
        if tam % i == 0:
            tam = tam // i
            dem = dem + 1
        else:
            break 
    for k in range(dem):
        print(i, end=" ")