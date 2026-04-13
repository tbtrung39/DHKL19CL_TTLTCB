a = [2,-4,1,9,-3,6,3,-2,6,8]
n = 10
#Tính tổng các phần tử
tong = sum(a)
print(f"Tổng các phần tử: {tong}")
# Đếm số phần tử dương và tổng của chúng
dem_duong = 0
tong_duong = 0
for i in range(n):
    if a[i] > 0:
        dem_duong = dem_duong + 1
        tong_duong = tong_duong + a[i]
print(f"Số phần tử dương: {dem_duong}")
print(f"Tổng các phần tử dương: {tong_duong}")
# Tìm vị trí phần tử âm đầu tiên
vitri_am = -1
for i in range(n):
    if a[i] < 0:
        vitri_am = i
        break
print(f"Vị trí phần tử âm đầu tiên: {vitri_am}")
# Tìm vị trí phần tử dương cuối cùng
vitri_duong = -1
for i in range(n-1, -1, -1):
    if a[i] > 0:
        vitri_duong = i
        break
print(f"Vị trí phần tử dương cuối cùng: {vitri_duong}")
# Tìm vị trí phần tử lớn nhất và vị trí xuất hiện cuối cùng của nó
max_value = a[0]
vitri_max = 0
for i in range(1, n):
    if a[i] > max_value:
        max_value = a[i]
        vitri_max = i
print(f"Vị trí phần tử lớn nhất: {vitri_max}")
print(f"Giá trị phần tử lớn nhất: {max_value}")