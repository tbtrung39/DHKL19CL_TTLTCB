import random
a= [random.randint(1,99999) for _ in range(1000)]

#sorted 
sorted = sorted(a)

#no sorted
A = a.copy()
for i in range(len(A)):
    for j in range(len(A)-i-1):
        if A[j] > A[j+1]:
            A[j] , A[j+1] = A[j+1] , A[j]
print(A)
