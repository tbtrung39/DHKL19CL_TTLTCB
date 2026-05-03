n = input("Nhap so phan tu n: ")
n = int(n)
a = []
i = 0
while i < n:
    x = input("a[" + str(i) + "]: ")
    x = int(x)
    a.append(x)
    i = i + 1
dem = 0
print("Cac cap chi so(i,j): ")
i = 0
while i < n:
    j = i + 1
    while j < n:
        if a[i] + 1 == a[j]:
            print("(" , i , "," , j ,")", end = " ")
            dem = dem + 1
        j = j + 1
    i = i + 1
print()
print("So cap tim duoc: ", dem)