A = {10, "Hello", 3.14, 42, "Python", 5.5, 0}

dem_int = 0
dem_float = 0
dem_str = 0

for phan_tu in A:
    if type(phan_tu) is int:
        dem_int += 1
    elif type(phan_tu) is float:
        dem_float += 1
    elif type(phan_tu) is str:
        dem_str += 1

print("Tập hợp A:", A)
print(f"Số lượng số nguyên: {dem_int}")
print(f"Số lượng số thực: {dem_float}")
print(f"Số lượng chuỗi ký tự: {dem_str}")
    