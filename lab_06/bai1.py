a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# Tính tổng các phần tử
tong = sum(a)
print("Tổng = ", tong)
# Đếm số lượng các số hạng dương và tính tổng của các số hạng dương
dem = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem += 1
        tong_duong += x
print("Số lượng số dương: ", dem)
print("Tổng các số hạng dương: ", tong_duong)
# Tìm vị trí của phần tử âm đầu tiên 
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
print("Vị trí phần tử âm đầu tiên: ", vi_tri_am_dau)
# Tìm vị trí phần tử dương cuối cùng
vi_tri_duong_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
print("Vị trí phần tử dương cuối cùng: ", vi_tri_duong_cuoi)
# Tìm phần tử lớn nhất và vị trị phần tử lớn nhất cuối cùng
max_val = max(a)
vi_tri_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] == max_val:
        vi_tri_cuoi = i
        break
print("Phần tử lớn nhất: ", max_val)
print("Vị trí cuối của nó: ", vi_tri_cuoi)
