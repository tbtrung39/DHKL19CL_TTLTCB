n = input("Nhập n: ")
n = int(n)
tong = 0
for i in range(1, n + 1):
    tong = tong + 1/i
print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", tong)