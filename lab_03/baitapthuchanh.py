# Bài 7: Tổng nghịch đảo
s_bai7 = sum(1/i for i in range(1, n + 1))
print(f"Bài 7: S = {s_bai7:.4f}")
# Bài 8: Tổng cơ bản
s1 = sum(range(1, n + 1))
s2 = sum(2*i + 1 for i in range(0, n + 1)) # 1+3+...+(2n+1)
s3 = sum(2*i for i in range(1, n + 1))
print(f"Bài 8: S1={s1}, S2={s2}, S3={s3}")
# Bài 9: Tổng lũy thừa dùng vòng lặp for
s4, s5, s6 = 0, 0, 0
for i in range(1, n + 1):
    s4 += i**2
    s5 += (2*i - 1)**3 # Số lẻ: 1, 3, 5...
    s6 += (2*i)**4     # Số chẵn: 2, 4, 6...
print(f"Bài 9: S4={s4}, S5={s5}, S6={s6}")
#bài 10
def phan_tich_thua_so(n):
    print(f"{n} = ", end="")
    temp = n
    i = 2
    kq = []
    while i * i <= temp:
        while temp % i == 0:
            kq.append(str(i))
            temp //= i
        i += 1
    if temp > 1:
        kq.append(str(temp))
    print(" * ".join(kq))
#bài 11
def ve_tam_giac_rong(n):
    for i in range(1, n + 1):
        # In khoảng trắng cách lề
        print(" " * (n - i), end="")
        # In các ngôi sao
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()