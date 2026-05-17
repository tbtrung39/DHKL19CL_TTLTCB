a = [1, 2, 3, 2, 4]
n = len(a)
count = 0
print("\nBài 16:")
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            count += 1
            print(f"Cặp ({i}, {j}): {a[i]} + 1 = {a[j]}")
print(f"Tổng số cặp: {count}")