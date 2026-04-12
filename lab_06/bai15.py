ds = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    name = input("Name: ")
    age = int(input("Age: "))
    score = int(input("Score: "))
    ds.append((name, age, score))
ds_sorted = sorted(ds, key=lambda x: (x[0], x[1], x[2]))
print(ds_sorted)