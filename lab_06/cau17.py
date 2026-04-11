n = int(input("Nhập n: "))

don_vi = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for row in don_vi:
    print(row)