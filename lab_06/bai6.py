#viet program sinh ra mot day list tu nhien gom 1000 so tu nhien, nam ngau nhien trong khoang [1,99999]
import random
n = []
for i in range(1000):
    n.append(random.randint(1, 99999))
print("Danh sach 1000 so tu nhien: ", n)

#su dung ham sorted de sap xep danh sach n theo thu tu tang dan
n_sorted = sorted(n)
print("Danh sach sau khi sap xep tang dan: ", n_sorted)
#khong su dung ham sorted de sap xep danh sach n theo thu tu tang dan
for i in range(len(n)-1):
    for j in range(i+1, len(n)):
        if n[i] > n[j]:
            n[i], n[j] = n[j], n[i]
print("Danh sach sau khi sap xep tang dan: ", n)
