n = int(input("Nhập n: "))
fib = [0, 1]
for i in range(2, n + 1):
    fib.append(fib[i-1] + fib[i-2])
print(", ".join([str(x) for x in fib]))