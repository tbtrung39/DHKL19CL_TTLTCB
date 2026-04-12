# Các phần tử của B chia hết cho 3 nhưng không chia hết cho 5
A = list(map(int, input().split()))
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(B)
# Tạo một danh sách C với các phần tử  là bình phương của danh sách A
C = [x**2 for x in A]
print(C)
# Tạo danh sách D và lấy ngẫu nhiên từ A và chia hết cho 3
import random
D = [x for x in A if x % 3 == 0]
D_random = random.sample(D, min(len(D), 3))
print(D_random)