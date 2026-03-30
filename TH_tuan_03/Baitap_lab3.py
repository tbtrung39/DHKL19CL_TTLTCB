#9
n = int(input("Nhập n (>0): "))
while n <= 0:
    n = int(input("Nhập lại n (>0): "))

S4 = 0
for i in range(1, n+1):
    S4 += i**2
S5 = 0
for i in range(1, n+1):
    S5 += (2*i - 1)**3
S6 = 0
for i in range(1, n+1):
    S6 += (2*i)**4

print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)
#10
n = int(input("Nhập số nguyên dương: "))
i = 2
print("Phân tích:", end=" ")

while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n //= i
    else:
        i += 1
#11
n = int(input("Nhập n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()