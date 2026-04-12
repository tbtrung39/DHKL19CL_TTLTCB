import random

# Bài 5: Sinh 1000 số ngẫu nhiên [1, 99999]
A = [random.randint(1, 99999) for _ in range(1000)]

# Bài 6: Sắp xếp theo 2 cách
# Cách 1: Dùng hàm sorted()
A_sorted = sorted(A)

# Cách 2: Không dùng sorted (Dùng thuật toán nổi bọt - Bubble Sort)
A_manual = A[:] # Tạo bản sao để không hỏng danh sách gốc
n = len(A_manual)
for i in range(n):
    for j in range(0, n - i - 1):
        if A_manual[j] > A_manual[j + 1]:
            A_manual[j], A_manual[j + 1] = A_manual[j + 1], A_manual[j]

print("Sắp xếp thủ công hoàn tất.")