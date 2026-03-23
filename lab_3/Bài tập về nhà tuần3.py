# Bài 6
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += i**3
print("S =", S)

#Bài 7
n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += 1/i
print("S =", S)

#Bài 8
while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
    print("Nhập lại!")
S1 = 0
S2 = 0
S3 = 0
for i in range(1, n+1):
    S1 = S1 + i         
    S2 = S2 + (2*i - 1)  
    S3 = S3 + (2*i)     
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)

#Bài 9
while True:
    n = int(input("Nhập n (>0): "))
    if n > 0:
        break
    print("Nhập lại!")
S4 = 0
for i in range(1, n+1):
    S4 += i * i
S5 = 0
i = 1
while i <= n:
    so_le = 2*i - 1
    S5 += so_le**3
    i += 1
S6 = 0
i = 1
while i <= n:
    so_chan = 2*i
    S6 += so_chan**4
    i += 1
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)

#Bài 10
n = int(input("Nhập số nguyên dương n: "))
i = 2
while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n = n // i
    else:
        i += 1

#Bài 11
#a
n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#b
n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#c
n = int(input("Nhập n: "))
for i in range(1, n + 1):
    # khoảng trắng
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        if j == 1 or j == 2*i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Bài 12        
n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    a.append(x)
tong = sum(x for x in a if x % 3 == 0)
print("Tổng =", tong)