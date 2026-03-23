n = int(input("Nhập n: "))
for hang in range(1, n + 1):
    for cot in range(2*n - 1):
        if n - hang <= cot <= n + hang - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()