def sum_1_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_1_to_n(n - 1)
n = int(input("Nhap so tu nhien N: "))
result = sum_1_to_n(n)
print("Tong S1 = 1 + 2 + ... + n =", result)
# Giai thich:
# vd nhap n = 3 -> sum_1_to_n(3) -> 3 + sum_1_to_n(2) -> 3 + (2 + sum_1_to_n(1)) -> 3 + (2 + 1) -> 6
# chay print ket qua