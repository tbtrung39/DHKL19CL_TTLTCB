n = input("Nhập số phần tử n: ")
n = int(n)
a = []
for i in range(n):
    x = input(f"Nhập phần tử thứ {i}: ")
    x = int(x)
    a.append(x)

# Tìm phần tử lớn thứ hai và vị trí đạt giá trị lớn thứ hai
max1 = a[0]
for i in range(1, n):
    if a[i] > max1:
        max1 = a[i]

max2 = None
vi_tri = -1
for i in range(n):
    if a[i] != max1:
        if max2 is None or a[i] > max2:
            max2 = a[i]
            vi_tri = i
print("Gía trị lớn thứ 2: ", max2)
print("Vị trí đạt giá trị lớn thứ 2: ", vi_tri)

#Tính số lượng số dương liên tiếp nhiều nhất
dem = 0
max_dem = 0
for i in range(n):
    if a[i] > 0:
        dem = dem + 1
        if dem > max_dem:
            max_dem = dem
    else:
        dem = 0
print("Số lượng số dương liên tiếp nhiều nhất: ", max_dem)

# Tính số lượng các số dương liên tiếp có tổng lớn nhất
tong = 0
max_tong = 0
dem = 0
dem_max = 0
for i in range(n):
    if a[i] > 0:
        tong = tong + a[i]
        dem = dem + 1
    else:
        if tong > max_tong:
            max_tong = tong
            dem_max = dem
        tong = 0
        dem = 0 
if tong > max_tong:
    max_tong = tong
    dem_max = dem
print("Số lượng các số dương liên tiếp có tổng lớn nhất: ", dem_max)
