X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))
matrix = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    matrix.append(row)
print(matrix)