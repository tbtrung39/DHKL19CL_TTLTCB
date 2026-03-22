n = input("Nhập n (>0): ")
n = int(n)
while n <= 0:
    n = input("Nhập lại n (>0): ")
    n = int(n)
#a
S1 = 0
for i in range(1, n + 1):
    S1 = S1 + i
print("Tổng S1 =", S1)
#b
S2 = 0
for i in range(n):
    S2 = S2 + (2*i + 1)
print("Tổng S2 =", S2)
#c
S3 = 0 
for i in range(1, n + 1):
    S3 = S3 + (2*i)
print("Tổng S3 =", S3)