n = []

while True:
    x = int(input("Nhap so nguyen (nhap q de thoat): "))
    if x == 'q':
        break
    n.append(x)

#a
b = [x for x in n if x % 3 == 0 and x % 5 != 0 ]
print("Cac so chia het cho 3 nhung khong chia het cho 5: ", b)

#cac phan tu la binh phuong cua danh sach n
c = [x**2 for x in n]
print("Cac phan tu la binh phuong cua danh sach n: ", c)

#lay cac phan tu ngau nhien trong danh sach n ma chia het cho 3
import random
d = [x for x in n if x % 3 == 0]
if len(d) > 0:
    random_element = random.choice(d)
    print("Phan tu ngau nhien trong danh sach n ma chia het cho 3: ", random_element)
else:
    print("Khong co phan tu nao trong danh sach n ma chia het cho 3.")
