# a. Tạo mới
n = int(input("\nNhập số NV (Bài 19): "))
nv_dict = {}
for _ in range(n):
    ma = input("Mã NV (4 ký tự): ")
    nv_dict[ma] = {
        "ten": input("Tên: "),
        "nam_sinh": int(input("Năm sinh: ")),
        "luong": float(input("Lương: "))
    }

# b. Thêm nhân viên
ma_them = input("Nhập mã NV cần thêm: ")
nv_dict[ma_them] = {"ten": "Mới", "nam_sinh": 2000, "luong": 5000000}

# c. Tìm kiếm nhân viên tên x
x = input("Nhập tên cần tìm: ")
for ma in nv_dict:
    if nv_dict[ma]['ten'] == x:
        print(f"Tìm thấy mã: {ma}")

# d. Tăng lương cho mã y
y = input("Nhập mã y để tăng lương: ")
if y in nv_dict:
    nv_dict[y]['luong'] += 1000000

# e. Xóa nhân viên mã z
z = input("Nhập mã z để xóa: ")
if z in nv_dict:
    del nv_dict[z]

# f. Sắp xếp giảm dần theo năm sinh (Chuyển sang list để sắp xếp)
ds_nv = []
for ma in nv_dict:
    item = nv_dict[ma]
    item['ma'] = ma
    ds_nv.append(item)

for i in range(len(ds_nv)):
    for j in range(0, len(ds_nv) - i - 1):
        if ds_nv[j]['nam_sinh'] < ds_nv[j+1]['nam_sinh']:
            ds_nv[j], ds_nv[j+1] = ds_nv[j+1], ds_nv[j]

print("Kết quả sắp xếp năm sinh giảm dần:")
for nv in ds_nv:
    print(nv)
