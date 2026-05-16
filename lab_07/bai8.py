A = {1, 2.5, "abc", 7, 8.2, "hello"}
so_nguyen = 0
so_thuc = 0
chuoi = 0
for i in A:
    if type(i) == int:
        so_nguyen = so_nguyen + 1
    elif type(i) == float:
        so_thuc = so_thuc + 1
    elif type(i) == str:
        chuoi = chuoi + 1
print("Số nguyên: ", so_nguyen)
print("Số thực: ", so_thuc)
print("Chuỗi: ", chuoi)