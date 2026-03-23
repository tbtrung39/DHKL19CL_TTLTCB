n = int(input("Nhập n: "))
for hang in range(1, n + 1):
    for cot in range(1, n + 1):
        if cot == 1 or cot == hang or hang == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()