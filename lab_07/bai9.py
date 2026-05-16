n = int(input("Nhập số tự nhiên n: "))
A = set()
B = set()
for i in range(2, n + 1):
    nt = True
    for j in range(2, i):
        if i % j == 0:
            False
    if nt == True:
        if n % i == 0:
            A.add(i)
        else:
            B.add(i)
print("Tập A: ", A)
print("Tập B: ", B)
        