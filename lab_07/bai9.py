# a. Nhập n vào bàn phím:
n = int(input("Nhập số lượng phần tử trong tập hợp A: "))
# b. Tạo 2 tập hợp A và B , trong đó A là ước của n; tập hợp B bao gồm các số nguyên tố bé hơn n và ko phải ước
A = set()
B = set()
for i in range(1, n + 1):
    if n % i == 0:
        A.add(i)
for i in range(2, n):
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1)) and n % i != 0:
        B.add(i)
print("Tập hợp A (ước của n):", A)
print("Tập hợp B (số nguyên tố bé hơn n và không phải ước):", B)