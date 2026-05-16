Numbers = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    x = int(input("Nhập số: "))
    Numbers.append(x)
a = set(Numbers)
print("Danh sách: ", Numbers)
print("Tập hợp: ", a)
