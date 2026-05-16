n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("a[" + str(i) + "] = "))
    a.append(x)
dem = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            print("(" + str(i) + "," + str(j) + ")")
            dem = dem + 1
print("Số cặp tìm được:", dem)