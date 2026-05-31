def luy_thua(a,n):
    if n == 0:
        return 1
    return a * luy_thua(a,n-1)
a = int(input("Nhập a: "))
n = int(input("Nhập n: "))
print("Kết quả: ", luy_thua(a,n))