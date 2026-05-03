n = input("Nhập n: ")
n = int(n)
A = set()
B = set()
i = 2
while i <= n:
    la_snt = True
    j = 2
    while j <= i // 2:
        if i % j == 0:
            la_snt = False
            break
        j = j + 1
    if la_snt:
        if n % i == 0:
            A.add(i)
        elif i < n:
            B.add(i)
    i = i + 1
print("Tập hợp A (ước nguyên tố của n ):",A)
print("Tập hợp B (số nguyên tố nhỏ hơn n và không là ước của n ):",B)