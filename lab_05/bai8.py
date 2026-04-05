import string

s = input("Nhập đoạn văn: ").lower()

tu = input("Nhập từ cần tìm: ").lower()

for dau in string.punctuation:
    s = s.replace(dau, " ")

ds_tu = s.split()

dem = 0
for word in ds_tu:
    if word == tu:
        dem += 1
print("Số lần xuất hiện:", dem)