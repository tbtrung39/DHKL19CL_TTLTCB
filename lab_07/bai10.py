m = input("Nhập m: ")
n = input("Nhập n: ")
A = set(m)
B = set(n)
chung = A & B
tong = 0
for i in chung:
    tong = tong + int(i)
print("Các chữ số chung: ", chung)
print("Tổng: ", tong)