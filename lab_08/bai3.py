def kt_nguyento(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
n = input("Nhap vao n: ")
n = int(n)
for i in range(1,n):
    if kt_nguyento(i):
        print(i, end=' ')