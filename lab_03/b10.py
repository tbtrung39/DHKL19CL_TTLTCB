n = int(input("Nhập n (>0): "))

i = 2
print(f"{n} = ", end="")

while n > 1:
    if n % i == 0:
        print(i, end="")
        n //= i
        if n > 1:
            print(" * ", end="")
    else:
        i += 1