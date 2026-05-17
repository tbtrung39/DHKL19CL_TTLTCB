def tim_nghiem(N,n,k = []):
    if n == 1:
        print(k + [N])
        return
    for i in range(N + 1):
        tim_nghiem(N - i, n - 1, k + [i])
N = input("Nhap N: ")
N = int(N)
n = input("Nhap so bien n: ")
n = int(n)
tim_nghiem(N, n)
# Giải thích:
# vd nhập N = 3, n = 2 -> tim_nghiem(3, 2, []) -> i = 0 -> tim_nghiem(3, 1, [0]) -> print([0, 3])
# -> i = 1 -> tim_nghiem(2, 1, [1]) -> print([1, 2])
# -> i = 2 -> tim_nghiem(1, 1, [2]) -> print([2, 1])
# -> i = 3 -> tim_nghiem(0, 1, [3]) -> print([3, 0])
