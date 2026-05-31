import random
n = int(input("Nhập n: "))
A = []
for i in range(1, n + 1):
    A.append(i)
result = []
while len(A) > 0:
    x = random.choice(A)
    result.append(x)
    A.remove(x)
print("Hoán vị ngẫu nhiên:", result)