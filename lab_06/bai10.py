import random
a = [random.randint(0, 200) for _ in range(20)]
kq = [x for x in a if x % 5 == 0 and x % 7 == 0]
print("List ban đầu: ", a)
print("Kết quả: ", kq)