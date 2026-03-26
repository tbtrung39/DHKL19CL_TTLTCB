n = int(input(' nhap n: '))
if n <= 0:
    print('nhap lai ')

    n = int(input('nhap lai n(n>0): '))
S1 = 0
for i in range(1,n+1):
    S1 = S1+ i
 
S2 = 0
for i in range(1,n+1):
    S2= S2 + (2*i+1)

S3= 0
for i in range (1, n+1):
    S3 = S3 + 2*i

print(S1)
print(S2)
print(S3)
