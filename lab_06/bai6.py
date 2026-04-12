import random

A = []
for i in range(1000):
    A.append(random.randint(1, 99999))

B = sorted(A)
print("Sorted():", B)

for i in range(len(A)):
    for j in range(len(A) - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

print("Không dùng sorted():", A)