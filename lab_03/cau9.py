n = int(input(' nhap n: '))
if n <= 0:
    print('nhap lai ')
    n = int(input('nhap lai n(n>0): '))

S4=0
S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2

S5 = 0
for i in range(0, n + 1):
    S5 += (2 * i + 1) ** 3

S6 = 0
for i in range(1, n + 1):
    S6 += (2 * i) ** 4

print(f"S4 = {S4}")
print(f"S5 = {S5}")
print(f"S6 = {S6}")


