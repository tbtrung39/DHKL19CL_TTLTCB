import random
n = input("Nhap n: ")
n = int(n)
A = list(range(1, n + 1))
kq = []
while len(A) > 0:
    x = random.choice(A)
    kq.append(x)
    A.remove(x)
print("Hoan vi ngau nhien:", kq)
# Giải thích:
# vd nhập n = 3 -> A = [1, 2, 3] -> random.choice(A) = 2 -> kq = [2] -> A = [1, 3]
# -> random.choice(A) = 1 -> kq = [2, 1] -> A = [3]
# -> random.choice(A) = 3 -> kq = [2, 1, 3] -> A = []
# -> print("Hoan vi ngau nhien:", [2, 1, 3])    