n = []
while True:
    x = int(input("Nhap so tu nhien (nhap 0 de thoat): "))
    if x == 0:
        break
    n.append(x)

#chen danh sach [1,2,3] vao dau danh sach n
n = [1, 2, 3] + n
print("Danh sach sau khi chen [1,2,3] vao dau: ", n)
#chen [1,2,3] vao cuoi danh sach n
n = n + [1, 2, 3]
print("Danh sach sau khi chen [1,2,3] vao cuoi: ", n)
#chen [1,2,3] vao vi tri thu 5 trong danh sach n
if len(n) >= 5:
    n = n[:4] + [1, 2, 3] + n[4:]
print("Danh sach sau khi chen [1,2,3] vao vi tri thu 5: ", n)

#xoa phan tu k, nhap tu ban phim, neu k khong co trong danh sach thi thong bao khong co
k = int(input("Nhap so k can xoa: "))
if k in n:
    n.remove(k)
    print("Danh sach sau khi xoa phan tu k: ", n)
else:
    print("Khong co phan tu k trong danh sach.")

#sap xep danh sach n theo thu tu tang dan
for i in range(len(n)-1):
    for j in range(i+1, len(n)):
        if n[i] > n[j]:
            n[i], n[j] = n[j], n[i]
print("Danh sach sau khi sap xep tang dan: ", n)
#theo thu tu giam dan
for i in range(len(n)-1):
    for j in range(i+1, len(n)):
        if n[i] < n[j]:
            n[i], n[j] = n[j], n[i]
print("Danh sach sau khi sap xep giam dan: ", n)
