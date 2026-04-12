a = [2,-4,1,9,-3,6,3,-2,6,8]

#tinh tong
tong = 0
for i in a:
    tong += i
print("Tong cac phan tu trong mang la: ", tong)

#dem so hang duong va tinh tong so hang duong
dem_duong = 0
tong_duong = 0
for i in a:
    if i > 0:
        dem_duong += 1
        tong_duong += i
print("Tong cac phan tu duong trong mang la: ", tong_duong)
print("So luong phan tu duong trong mang la: ", dem_duong)

#tim vi tri phan tu am dau tien trong a
vi_tri_am_dau_tien = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau_tien = i
        break
if vi_tri_am_dau_tien != -1:
    print("Vi tri phan tu am dau tien trong mang la: ", vi_tri_am_dau_tien)
else:
    print("Khong co phan tu am trong mang.")

#vi tri cua phan tu duong cuoi cung trong a
vi_tri_duong_cuoi_cung = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi_cung = i
        break
if vi_tri_duong_cuoi_cung != -1:
    print("Vi tri phan tu duong cuoi cung trong mang la: ", vi_tri_duong_cuoi_cung)
else:
    print("Khong co phan tu duong trong mang.")

#tim phan tu lon nhat trong a va tri tri cua no
max_value = a[0]
max_index = 0
for i in range(1, len(a)):
    if a[i] > max_value:
        max_value = a[i]
        max_index = i
print("Phan tu lon nhat trong mang la: ", max_value)
print("Vi tri cua phan tu lon nhat trong mang la: ", max_index)


