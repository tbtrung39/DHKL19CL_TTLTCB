n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)
b = list(map(lambda x: x ** 2, a))
print("List ban đầu:", a)
print("List bình phương:", b)