def la_so_nguyen_to(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

n = int(input("Nhập số tự nhiên n: "))
A = set()
B = set()
for i in range(2, n):
    if la_so_nguyen_to(i):
        if n % i == 0:
            A.add(i)  
        else:
            B.add(i) 
if la_so_nguyen_to(n):
    A.add(n)

print(f"Tập hợp A (ước nguyên tố của {n}):", A)
print(f"Tập hợp B (số nguyên tố < {n} và không là ước):", B)