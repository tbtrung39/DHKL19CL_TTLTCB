X = input("Nhập X: ")
X=int(X)
Y = input("Nhập Y: ")
Y=int(Y)
matrix = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    matrix.append(row)
print(matrix)