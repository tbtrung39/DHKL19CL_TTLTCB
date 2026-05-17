def sum_even_numbers(n):
    if n == 1:
        return 2
    else:
        return 2 * n + sum_even_numbers(n - 1)
n = int(input("Nhap so tu nhien N: "))
result = sum_even_numbers(n)
print("Tong S2 = 2 + 4 + ... + 2n =", result)
# Giai thich:
# vd nhap n = 3 -> sum_even_numbers(3) -> 2*3 + sum_even_numbers(2) -> 6 + (2*2 + sum_even_numbers(1)) -> 6 + (4 + 2) -> 12
# chay print ket qua