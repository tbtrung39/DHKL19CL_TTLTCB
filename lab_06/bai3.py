#nhap vao danh sach cac phan tu la so tu nhien cho den khi nhap vao so 0
n = []
while True:
    x = int(input("Nhap so tu nhien (nhap 0 de thoat): "))
    if x == 0:
        break
    n.append(x)

#chuyen cac phan tu  duong len dau danh sahc
duong = []
am = []
for i in n:
    if i > 0:
        duong.append(i)
    else:
        am.append(i)
n = duong + am
print("Danh sach sau khi chuyen cac phan tu duong len dau: ", n)

# chen 1 so m nhap tu ban phim vao dau , cuoi danh sach va vi tri thu 5
m = int(input("Nhap so m: "))
n.insert(0, m)
n.append(m)
if len(n) >= 5:
    n.insert(4, m)
print("Danh sach sau khi chen so m vao dau, cuoi va vi tri thu 5: ", n)
