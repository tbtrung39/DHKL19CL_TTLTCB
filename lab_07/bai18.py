thisinh = {}
n = int(input("Nhập số thí sinh: "))
for i in range(n):
    sbd = input("Số báo danh: ")
    ten = input("Họ tên: ")
    diem = float(input("Điểm thi: "))
    thisinh[sbd] = {
        "ten": ten,
        "diem": diem
    }
tim = input("Nhập số báo danh cần tìm: ")
if tim in thisinh:
    print("Họ tên:", thisinh[tim]["ten"])
    print("Điểm:", thisinh[tim]["diem"])
else:
    print("Không tồn tại, nhập thêm mới")
    ten = input("Họ tên: ")
    diem = float(input("Điểm thi: "))
    thisinh[tim] = {
        "ten": ten,
        "diem": diem
    }
print(thisinh)