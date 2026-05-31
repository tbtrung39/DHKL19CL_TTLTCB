n = int(input("Nhập số lượng phần tử n: "))
danh_sach = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
binh_phuong_so_le = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, danh_sach)))

print("Danh sách ban đầu:", danh_sach)
print("Bình phương các số lẻ trong danh sách:", binh_phuong_so_le)