n = input("Nhập số hàng n: ")
n = int(n)
for dong in range(1, n + 1):
    for cot in range(n - dong):
        print(" ", end="")
    for cot in range(1, 2*dong):
        if cot == 1 or cot == 2*dong -1 or dong == n :
            print("*", end="")
        else:
            print(" ", end="")
    print()
