import random
s = input("Nhập các ký tự chữ và số: ")
A = set()
B = set()
while len(A) < 5:
    A.add(random.choice(s))
while len(B) < 5:
    B.add(random.choice(s))
C = A & B
print("Tập hợp A: ",A)
print("Tập hợp B: ",B)
print("Các phần tử chung của A và B: ",C)
