# a. Tạo mới từ điển nhân viên (Khởi tạo dữ liệu mẫu)
nhan_vien_db = {
    "1001": {"ho_ten": "Tran Van An        ", "nam_sinh": 1995, "luong": 15000000},
    "1002": {"ho_ten": "Le Thi Binh         ", "nam_sinh": 1998, "luong": 12000000},
    "1003": {"ho_ten": "Nguyen Cao Cuong    ", "nam_sinh": 1992, "luong": 20000000}
}

# b. Thêm nhân viên mới từ bàn phím
print("\n--- b. Thêm nhân viên mới ---")
while True:
    ma_nv = input("Nhập mã nhân viên mới (4 ký tự số): ")
    if len(ma_nv) == 4 and ma_nv.isdigit():
        break
    print("Mã nhân viên phải gồm đúng 4 ký tự số!")

ho_ten = input("Nhập họ tên nhân viên: ").ljust(20) # Tự động điền dấu cách cho đủ 20 ký tự
nam_sinh = int(input("Nhập năm sinh: "))
luong = int(input("Nhập lương: "))

nhan_vien_db[ma_nv] = {"ho_ten": ho_ten, "nam_sinh": nam_sinh, "luong": luong}
print("Thêm nhân viên thành công!")

# c. Tìm kiếm nhân viên theo mã x
print("\n--- c. Tìm kiếm nhân viên ---")
x = input("Nhập mã nhân viên x cần tìm: ")
if x in nhan_vien_db:
    print(f"Tìm thấy: {nhan_vien_db[x]['ho_ten']} | Năm sinh: {nhan_vien_db[x]['nam_sinh']} | Lương: {nhan_vien_db[x]['luong']}")
else:
    print("Không tìm thấy nhân viên có mã vừa nhập.")

# d. Tăng lương 1.000.000 cho nhân viên có mã là y
print("\n--- d. Tăng lương cho nhân viên ---")
y = input("Nhập mã nhân viên y cần tăng lương: ")
if y in nhan_vien_db:
    nhan_vien_db[y]["luong"] += 1000000
    print(f"Đã tăng lương thành công! Lương mới của nhân viên {y} là: {nhan_vien_db[y]['luong']}")
else:
    print("Không tồn tại nhân viên này.")

# e. Xóa nhân viên có mã là z
print("\n--- e. Xóa nhân viên ---")
z = input("Nhập mã nhân viên z cần xóa: ")
if z in nhan_vien_db:
    del nhan_vien_db[z] 
    print(f"Đã xóa nhân viên có mã {z} ra khỏi danh sách.")
else:
    print("Mã nhân viên cần xóa không hợp lệ.")

# f. Sắp xếp từ điển giảm dần theo năm sinh
print("\n--- f. Danh sách nhân viên sắp xếp theo năm sinh giảm dần ---")
ma_nv_sap_xep = sorted(nhan_vien_db, key=lambda key: nhan_vien_db[key]["nam_sinh"], reverse=True)

for ma in ma_nv_sap_xep:
    nv = nhan_vien_db[ma]
    print(f"Mã: {ma} | Tên: {nv['ho_ten']} | Năm sinh: {nv['nam_sinh']} | Lương: {nv['luong']}")
