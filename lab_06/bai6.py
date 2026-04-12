import random
A = [random.randint(1, 99999) for _ in range(1000)]
# Cách 1:
B = sorted(A)
print("List sau khi sắp xếp xong: ")
print(B[:20])

# Cách 2:
for i in range(len(A)):
    for j in range(len(A) - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
print("List sau khi sắp xếp: ")
print(A[:20])