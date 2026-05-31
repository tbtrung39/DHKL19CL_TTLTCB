def tim_nghiem(n, N, kq=[]):
    if n == 1:
        print(kq + [N])
        return
    for i in range(1, N - n + 2):
        tim_nghiem(n - 1, N - i, kq + [i])
n = int(input("Nhập n: "))
N = int(input("Nhập N: "))
tim_nghiem(n, N)