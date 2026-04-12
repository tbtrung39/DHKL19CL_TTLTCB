A = [15, 3, 5, 9, 30] 
print("B:", [x for x in A if x % 3 == 0 and x % 5 != 0])
print("C:", [x**2 for x in A])
import random
print("D:", random.sample([x for x in A if x % 3 == 0], 1))