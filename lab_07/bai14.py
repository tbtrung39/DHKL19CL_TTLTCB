dict_binary = {}
for i in range(1, 101):
    # Thuật toán chuyển số thập phân sang nhị phân thủ công
    n = i
    s = ""
    if n == 0: s = "0"
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    dict_binary[i] = s

print("Bài 14 (5 phần tử đầu):")
for i in range(1, 6):
    print(f"{i}: {dict_binary[i]}")