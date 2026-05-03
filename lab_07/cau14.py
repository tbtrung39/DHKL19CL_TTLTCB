A ={}
i = 1
while i <= 100:
    n = i 
    nhi_phan = ""
    while n > 0:
        du = n % 2
        nhi_phan = str(du) + nhi_phan
        n = n // 2
    A[i] = nhi_phan
    i = i + 1
print(A)