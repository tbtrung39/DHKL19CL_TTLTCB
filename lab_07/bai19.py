nhanvien = {}
n = int(input("Nhập số nhân viên: "))
for i in range(n):
    ma = input("Mã nhân viên: ")
    ten = input("Họ tên: ")
    namsinh = int(input("Năm sinh: "))
    luong = int(input("Lương: "))
    nhanvien[ma] = {
        "ten": ten,
        "namsinh": namsinh,
        "luong": luong
    }
ma = input("\nNhập mã thêm: ")
ten = input("Họ tên: ")
namsinh = int(input("Năm sinh: "))
luong = int(input("Lương: "))
nhanvien[ma] = {
    "ten": ten,
    "namsinh": namsinh,
    "luong": luong
}
x = input("\nNhập mã cần tìm: ")
if x in nhanvien:
    print(nhanvien[x])
else:
    print("Không tìm thấy")
y = input("\nNhập mã cần tăng lương: ")
if y in nhanvien:
    nhanvien[y]["luong"] = nhanvien[y]["luong"] + 1000000
z = input("\nNhập mã cần xóa: ")
if z in nhanvien:
    del nhanvien[z]
ds = sorted(nhanvien.items(),
            key=lambda x: x[1]["namsinh"],
            reverse=True)
print("Danh sách sau cùng: ")
for ma, tt in ds:
    print(ma, tt)