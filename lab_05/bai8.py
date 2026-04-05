text = input("Nhập đoạn văn: ")
word = input("Nhập từ cần tìm: ")
ds = text.split()
dem = 0
for w in ds:
    if w == word:
        dem += 1
print("Số lần xuất hiện: ", dem)
