n = int(input("Nhập n: "))
for hang in range(n):
    for cot in range(2*n - 1):
        if cot == n - hang - 1 or cot == n + hang - 1 or hang == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()