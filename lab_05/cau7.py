str = input('nhap chuoi: ')
so = ""
for i in str:
    if i.isdigit():
        so = so + i
print(so)

n = int(so)
tong = 0 
for j in range(1,n):
    if n%i ==0:
        tong = tong+1

if tong == n :
    print('la so hoan hao')
else:
    print('khong phai so hoan hao')