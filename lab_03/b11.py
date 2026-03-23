n = int(input("Nhập n: "))

#Tam giác a
print("\nTam giác (a):")
for i in range(1, n + 2):
    print(" " * (n + 1 - i), end="")
    for j in range(1, i + 1):
        if i == 1 or i == n + 1 or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Tam giác b
print("\nTam giác (b):")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        if i == 1 or i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Tam giác c
print("\nTam giác (c):")
for i in range(1, n + 2):
    print(" " * (n + 1 - i), end="")
    for j in range(i):
        print("* ", end="")
    print()