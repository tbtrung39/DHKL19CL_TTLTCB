a = []
while True:
    x = input("Nhập số (0 để dừng): ")
    x = int(x)
    if x == 0:
        break
    a.append(x)
# Đưa các số dương lên đầu danh sách và in danh sách ra màn hình
duong = []
khac = []
for i in range(len(a)):
    if a[i] > 0:
        duong.append(a[i])
    else:
        khac.append(a[i])

a = duong + khac
print("Danh sách sau khi đưa các số dương lên đầu: ", a)

# Chèn một số m (m nhập vào từ bàn phím) vào đầu danh sách , cuối danh sách và vị trí thứ 5 của danh sách
m = input("Nhập số m: ")
m = int(m)
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(4, m)
else:
    a.append(m)
print("Danh sách sau khi chèn số m: ", a)