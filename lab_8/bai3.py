def kiem_tra_snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Nhập n: "))
print(f"Các số nguyên tố nhỏ hơn {num} là:")
for i in range(2, num):
    if kiem_tra_snt(i):
        print(i, end=" ")
print()