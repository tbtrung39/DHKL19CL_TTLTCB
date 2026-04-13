import random
a = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
b = random.sample(a, min(5,len(a)))
print("Các số ngẫu nhiên:", b)