n = int(input('nhap n: '))
fib = [0, 1]
fib = fib + [fib[i-1] + fib[i-2] for i in range(2, n)]

print(",".join(str(x) for x in fib[:n]))
