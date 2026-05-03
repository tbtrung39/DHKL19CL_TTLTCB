m = input("Nhập m: ")
n = input("Nhập n: ")
A = set(m)
B = set(n)
C = A&B
tong = 0
for i in C:
    tong = tong + int(i)
print("Các chữ số chung:",C)
print("Tổng các chữ số chung:",tong)