def tlt(a, n):
    if n == 0:
        return 1
    return a * tlt(a, n - 1)

# Nhập dữ liệu và in kết quả
a = int(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))

print(f"Kết quả {a}^{n} là:", tlt(a, n))