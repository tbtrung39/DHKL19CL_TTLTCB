Numbers = []
while True:
    n = input("Nhập số tự nhiên: ")
    n = int(n)
    if n == -1:
        break
    if n >= 0:
        Numbers.append(n)
A = set(Numbers)
print("Danh sach Numbers: ",Numbers)
print("Tập hợp A: ",A)
