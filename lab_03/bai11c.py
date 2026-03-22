n = input("Nhập n: ")
n = int(n)
k = 2*n - 2
for dong in range(1,n + 1):
    for cot in range(1,k + 1):
        print(end=" ")
    for cot in range(1, 2*dong):
        print("*", end=" ")    
    k = k - 2
    print()