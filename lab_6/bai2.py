n = int(input("Nhập số phần tử n: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i}: ")))

# 1. Tìm phần tử lớn thứ hai và vị trí
unique_sorted = sorted(list(set(a)), reverse=True)
if len(unique_sorted) < 2:
    print("Không có số lớn thứ hai")
else:
    max_2 = unique_sorted[1]
    positions = [i for i, x in enumerate(a) if x == max_2]
    print(f"Giá trị lớn thứ hai: {max_2}, tại các vị trí: {positions}")

# 2 & 3. Dãy số dương liên tiếp nhiều nhất và có tổng lớn nhất
max_count = current_count = 0
max_sum = current_sum = 0

for x in a:
    if x > 0:
        current_count += 1
        current_sum += x
        max_count = max(max_count, current_count)
        max_sum = max(max_sum, current_sum)
    else:
        current_count = 0
        current_sum = 0

print(f"Số lượng số dương liên tiếp nhiều nhất: {max_count}")
print(f"Tổng số dương liên tiếp lớn nhất: {max_sum}")