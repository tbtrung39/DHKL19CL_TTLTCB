n = int(input("\nNhập số lượng SV (Bài 17): "))
ds_sv = []

for i in range(n):
    ma = input("Mã SV: ")
    ten = input("Tên SV: ")
    diem = float(input("Điểm: "))
    # Làm tròn thủ công: cộng 0.5 rồi lấy phần nguyên
    diem_int = int(diem + 0.5)
    ds_sv.append({'ma': ma, 'ten': ten, 'diem': diem_int})

for i in range(len(ds_sv)):
    for j in range(0, len(ds_sv) - i - 1):
        if ds_sv[j]['diem'] < ds_sv[j+1]['diem']:
            # Hoán vị
            ds_sv[j], ds_sv[j+1] = ds_sv[j+1], ds_sv[j]

print("Danh sách sau sắp xếp:")
for sv in ds_sv:
    print(sv)