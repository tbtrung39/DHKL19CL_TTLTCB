import random
 
A = [random.randint(1, 99999) for _ in range(1000)]
print(f"Danh sách A (1000 số ngẫu nhiên trong [1,99999]):")
print(f"  10 phần tử đầu: {A[:10]}")
print(f"  10 phần tử cuối: {A[-10:]}")