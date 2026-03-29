s = input("Nhập đoạn văn: ")
tu = input("Nhập từ cần tìm: ")

dem = 0
i = 0
tu_hien_tai = ""

while i < len(s):
    if s[i] != " ":
        tu_hien_tai = tu_hien_tai + s[i]
    else:
        if tu_hien_tai == tu:
            dem = dem + 1
        tu_hien_tai = ""
    i = i + 1

if tu_hien_tai == tu:
    dem = dem + 1

print("Số lần xuất hiện:", dem)