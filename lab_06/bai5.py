A = []
for i in range(1000):
    A.append((i * 37 + 13) % 99999 + 1)
print(A)