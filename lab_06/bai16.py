# Nhập X và Y
chuoi_xy = input("Nhập X và Y (cách nhau bởi dấu phẩy): ")
X, Y = map(int, chuoi_xy.split(','))
mang_2_chieu = []
for i in range(X):
    hang = [] 
    for j in range(Y):
        hang.append(i * j)
    mang_2_chieu.append(hang)
print("Đầu ra:", mang_2_chieu)