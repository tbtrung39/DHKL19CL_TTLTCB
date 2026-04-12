a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# 1. Tính tổng các phần tử
tong = sum(a)
print(f"Tổng các phần tử: {tong}")

# 2. Đếm số dương và tổng các số dương
so_duong = [x for x in a if x > 0]
print(f"Số lượng số dương: {len(so_duong)}, Tổng số dương: {sum(so_duong)}")

# 3. Tìm vị trí phần tử âm đầu tiên
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
print(f"Vị trí phần tử âm đầu tiên: {vi_tri_am_dau}")

# 4. Tìm vị trí phần tử dương cuối cùng
vi_tri_duong_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
print(f"Vị trí phần tử dương cuối cùng: {vi_tri_duong_cuoi}")

# 5. Phần tử lớn nhất và vị trí lớn nhất cuối cùng
max_val = max(a)
vi_tri_max_cuoi = -1
for i in range(len(a)):
    if a[i] == max_val:
        vi_tri_max_cuoi = i
print(f"Giá trị lớn nhất: {max_val}, Vị trí cuối cùng của nó: {vi_tri_max_cuoi}")