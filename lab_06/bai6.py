
import random

A = [random.randint(1, 99999) for _ in range(1000)]
# Cách 1: Dùng hàm sorted()
A_sorted1 = sorted(A)
# Cách 2: Không dùng hàm sorted(), sử dụng thuật toán selection sort
A_sorted2 = A[:]
for i in range(len(A_sorted2)):
    min_index = i
    for j in range(i + 1, len(A_sorted2)):
        if A_sorted2[j] < A_sorted2[min_index]:
            min_index = j
    A_sorted2[i], A_sorted2[min_index] = A_sorted2[min_index], A_sorted2[i]
print(f"Cach 1 - Danh sách A đã sắp xếp (dùng sorted()): {A_sorted1[:10]}")
print(f"Cach 2 - Danh sách A đã sắp xếp (dùng selection sort): {A_sorted2[:10]}")
print(f"Kết quả 2 cách giống nhau: { A_sorted1 == A_sorted2 }")