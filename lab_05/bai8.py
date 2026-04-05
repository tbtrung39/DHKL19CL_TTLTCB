Str = input("Nhập đoạn văn: ").lower()
tu = input("Nhập từ cần tìm: ").lower()
for ky_tu in ".,!?;:\n":
    Str = Str.replace(ky_tu, " ")
danh_sach_tu = Str.split()
dem = 0 
for i in danh_sach_tu:
    if i == tu:
        dem = dem + 1
print("Số lần xuất hiện của từ", tu, "là:", dem)