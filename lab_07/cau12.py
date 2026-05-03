n = input("Nhập n: ")
n = int(n)
A = {}
i = 1
while i <= n:
    A[i] = i * i
    i = i + 1
print("Dictionary A:", A)