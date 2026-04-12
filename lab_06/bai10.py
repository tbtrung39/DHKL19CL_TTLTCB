import random
A = [random.randint(0, 200) for i in range(100)]
B = [x for x in A if x % 5 == 0 and x % 7 == 0]
print(B)