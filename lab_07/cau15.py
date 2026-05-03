n = input("Nhap n: ")
n = int(n)
list1 = []
list2 = []
i = 0
while i < n:
    x = input("Nhap x: ")
    x = int(x)
    list1.append(x)
    i = i + 1
i = 0
while i < n:
    ten = input("Nhap ten: ")
    list2.append(ten)
    i = i + 1
A = {}
i = 0
while i < n:
    A[list1[i]] = list2[i]
    i = i + 1
print("Dictionary A: ", A)