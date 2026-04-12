h = int(input("Nhập độ rộng (chiều cao) tam giác: "))
for i in range(1, h + 1):
    for j in range(1, 2 * h):
        if j == h - i + 1 or j == h + i - 1 or i == h:
            print("*", end="")
        else:
            print(" ", end="")
    print()