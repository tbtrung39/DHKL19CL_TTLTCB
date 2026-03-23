def bai9():
    print("--- BÀI 9 ---")
    n = int(input("Nhập số nguyên dương n: "))

    while n <= 0:
        n = int(input("n phải > 0. Vui lòng nhập lại n: "))

    S4 = 0
    S5 = 0
    S6 = 0

    for i in range(1, n + 1):
        S4 += i**2

    for i in range(0, n + 1):
        S5 += (2 * i + 1)**3

    for i in range(1, n + 1):
        S6 += (2 * i)**4

    print(f"Kết quả S4 = {S4}")
    print(f"Kết quả S5 = {S5}")
    print(f"Kết quả S6 = {S6}\n")


def bai10():
    print("--- BÀI 10 ---")
    n = int(input("Nhập số nguyên dương n: "))

    while n <= 0:
        n = int(input("n phải > 0. Vui lòng nhập lại n: "))

    print(f"Phân tích thừa số nguyên tố của {n} là: ", end="")

    i = 2
    first = True

    while n > 1:
        if n % i == 0:
            if not first:
                print(" x ", end="")
            print(i, end="")
            first = False
            n = n // i
        else:
            i += 1

    print("\n")


def bai11():
    print("--- BÀI 11 ---")
    n = int(input("Nhập độ rộng (số hàng) của tam giác n: "))

    print("\n(a) Tam giác vuông trái rỗng:")
    for i in range(n):
        if i == 0:
            print("*")
        elif i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (i - 1) + "*")

    print("\n(b) Tam giác cân rỗng:")
    for i in range(n):
        if i == 0:
            print(" " * (n - 1) + "*")
        elif i == n - 1:
            print("* " * n)
        else:
            print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")

    print("\n(c) Tam giác vuông phải rỗng:")
    for i in range(n):
        if i == 0:
            print(" " * (n - 1) + "*")
        elif i == n - 1:
            print("*" * n)
        else:
            print(" " * (n - i - 1) + "*" + " " * (i - 1) + "*")
    print("\n")


def bai12():
    print("--- BÀI 12 ---")
    container_code = input("Nhập chuỗi 10 ký tự container (VD: SUDU307007): ").upper()

    letter_values = {
        'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17,
        'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25,
        'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31, 'U': 32,
        'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
    }

    total_weight = 0

    for i in range(len(container_code)):
        char = container_code[i]

        if char.isalpha():
            value = letter_values.get(char, 0)
        else:
            value = int(char)

        weight = value * (2 ** i)
        total_weight += weight

    check_digit = total_weight % 11

    print(f"Tổng các trọng số = {total_weight}")
    print(f"Số kiểm tra của mã container {container_code} là: {check_digit}\n")

bai9()
bai10()
bai11()
bai12()
