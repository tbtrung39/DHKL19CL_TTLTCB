n = int(input('nhap 1 so tu nhien: '))
while n<0:
    print('nhap lai')
    n = int(input('nhap lai n: '))

print("Nhị phân:", bin(n)[2:])
