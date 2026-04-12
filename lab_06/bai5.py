#viet program sinh ra mot day list tu nhien gom 1000 so tu nhien, nam ngau nhien trong khoang [1,99999]
import random
n = []
for i in range(1000):
    n.append(random.randint(1, 99999))
print("Danh sach 1000 so tu nhien: ", n)
