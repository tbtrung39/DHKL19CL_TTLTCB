n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)
# Tìm số lớn thứ 2 và vị trí
b = list(set(a))
b.sort(reverse=True)
max2 = b[1]
vi_tri = []
for i in range(len(a)):
    if a[i] == max2:
        vi_tri.append(i)
print("Số lớn thứ 2: ", max2)
print("Vị trí: ", vi_tri)
# Số lượng số dương liên tiếp nhiều nhất
max_dem = dem = 0
for x in a:
    if x > 0:
        dem += 1
        max_dem = max(max_dem, dem)
    else:
        dem = 0
print("Dãy dương liên tiếp dài nhất: ", max_dem)
# Số lượng các số dương liên tiếp có tổng lớn nhất
max_sum = cur_sum = 0
for x in a:
    if x > 0:
        cur_sum += x
        max_sum = max(max_sum, cur_sum)
    else:
        cur_sum = 0
print("Tổng dãy dương lớn nhất: ", max_sum)
