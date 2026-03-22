n = input("Nhập n (>0): ")
n = int(n)
while n <= 0:
    n = input("Nhập lại n (>0): ")
    n = int(n)
#4
S4 = 0
for i in range(1, n + 1):
    S4 = S4 + i**2
print("Tổng S4 =", S4)
#5
S5 = 0
for i in range(n):
    S5 = S5 + (2*i + 1)**3
print("Tổng S5 =", S5)
#6
S6 = 0
for i in range(1, n + 1):
    S6 = S6 + (2*i)**4
print("Tổng S6 =", S6)