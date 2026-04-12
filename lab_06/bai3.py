a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)
# Chuyển số dương lên đầu 
a = [x for x in a if x > 0] + [x for x in a if x <= 0]
print(a)
# Chèn m vào đầu, cuối, vị trí thứ 5 của danh sách 
m = int(input("Nhập m: "))
a.insert(0, m)  # Đầu 
a.append(m)     # Cuối
if len(a) >= 5:
    a.insert(4, m)
print(a)