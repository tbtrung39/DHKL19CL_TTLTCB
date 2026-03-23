n = input("Nhap so n: ")
n = int(n)
tong = 1
for i in range(0,n+1):
    tich = 1
    for j in range(i+1):
        ct = 2*(i+1) / (2*i+3)
        tich = tich * ct
    tong = tong + tich
print(tong)


