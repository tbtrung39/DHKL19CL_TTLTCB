# Nhập n và kiểm tra điều kiện
while True:
    n = int(input("Nhap n: (n > 0): "))
    if n > 0:
        break
    print(" n không hợp lệ, xin nhập lại ")

#a:
S4 = 0
for i in range(1, n+1):
    S4 += i**2
print(f"Tổng S4 = {S4}")
#b:
S5 = 0
for i in range(1, n+1):
    S5 += (2*i + 1)**3
print(f"Tổng S5 = {S5}")
#c:
S6 = 0
for i in range(1, n+1):
    S6 += (2*i)**4
print(f"Tổng S6 = {S6}")


