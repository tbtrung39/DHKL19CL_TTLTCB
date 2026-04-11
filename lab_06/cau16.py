X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

mang = [[i*j for j in range(Y)] for i in range(X)]
print("Mảng 2 chiều:", mang)