n = int(input("Nhap mot so: "))
tong = 0
n = abs(n) 

while n > 0:
    tong = tong + (n % 10)
    n = n // 10

print(tong)