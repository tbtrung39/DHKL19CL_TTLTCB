n = int(input("Nhập số hàng: "))

#a
print("\n(a)")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#b
print("\n(b)")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == n - i + 1 or i == n or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#c
print("\n(c)")
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()