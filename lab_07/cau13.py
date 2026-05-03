W = input("Nhap chuoi W: ")
A ={}
n = len(W)
i = 0
while i < n:
    j = i + 1
    while j <= n:
        K = W[i:j]
        if K not in A:
            dem = 0
            t = 0
            while t <= n - len(K):
                if W[t:t+len(K)] == K:
                    dem = dem + 1
                t = t + 1
            A[K] = dem
        j = j + 1
    i = i + 1
print("Dictionary A: ", A)