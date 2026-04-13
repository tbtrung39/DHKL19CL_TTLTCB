n = input("Nhập n:")   
n = int(n)
# Tạo dãy Finonacci dùng list comprehension kết hợp
fib = [0,1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
fib = fib[:n]  # Lấy đúng n phần tử
ket_qua = ", ".join(str(num) for num in fib)
print(f"Dãy Fibonacci có {n} phần tử: {ket_qua}")
