n = int(input("Nhập số nguyên dương n: "))
print(f"{n} = ", end="")
i = 2
factors = []
temp = n
while i * i <= temp:
    while temp % i == 0:
        factors.append(str(i))
        temp //= i
    i += 1
if temp > 1:
    factors.append(str(temp))

print(" x ".join(factors))