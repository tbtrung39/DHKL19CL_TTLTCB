def sum_odd_numbers(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + sum_odd_numbers(n - 1)
n = int(input("Nhap so tu nhien N: "))
result = sum_odd_numbers(n)
print("Tong S3 = 1 + 3 + 5 + ... + (2n-1) =", result)
# Giai thich:
# vd nhap n = 3 -> sum_odd_numbers(3) -> (2*3 - 1) + sum_odd_numbers(2) -> 5 + ((2*2 - 1) + sum_odd_numbers(1)) -> 5 + (3 + 1) -> 9
# chay print ket qua