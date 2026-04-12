n = int(input("Nhập n: "))
f = [0, 1]
[f.append(f[-1] + f[-2]) for _ in range(n-1)]
print(*(f[:n+1]), sep=", ")