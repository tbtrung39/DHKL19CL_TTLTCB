import random
ds = [0,1,2,3,4,5,6,7,8,9]
A = set()
while len(A) < 5:
    x = random.choice(ds)
    A.add(x)
print("Danh sách: ", ds)
print("Tập hợp A:",A)