n = int(input('nhap so nguyen duong n: '))
if n <= 0:
    print('nhap lai')
    n = int(input('nhap lai n(n>0): '))
 
temp = n 
kq = ""

i = 2 
while i * i <= temp:
    dem = 0 
    while temp % i == 0:
        dem = dem + 1
        temp = temp // i 
    if dem > 0:
        if kq != "":
            kq = kq + " * "
        kq = kq + str(i) + "^" + str(dem)
    i = i + 1

if temp > 1:
    if kq != "":
        kq = kq + " * "
    kq = kq + str(temp) + "^1"

print(str(n) + " = " + kq)