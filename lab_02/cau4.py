n = int(input('nhap vao 1 sô nguyen: '))
n = abs(n)
if n >=100:
    print((n//100)%10)
else:
    print(0)