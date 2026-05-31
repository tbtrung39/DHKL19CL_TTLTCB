n = int(input("Nhập số lượng phần tử n: "))
danh_sach = []
for i in range(n):
    danh_sach.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
binh_phuong_list = list(map(lambda x: x**2, danh_sach))

print("Danh sách ban đầu:", danh_sach)
print("Danh sách sau khi bình phương:", binh_phuong_list)