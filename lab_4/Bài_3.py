import math

x_deg = float(input("Nhập x (độ): "))
x = math.radians(x_deg) 
sai_so = 0.0001

cos_x = 0
n = 0
while True:
    term = ((-1)**n * x**(2*n)) / math.factorial(2*n)
    cos_x += term
    if abs(term) < sai_so:
        break
    n += 1

print(f"cos({x_deg}) xấp xỉ là: {cos_x:.4f}")
print(f"Kiểm tra bằng thư viện: {math.cos(x):.4f}")