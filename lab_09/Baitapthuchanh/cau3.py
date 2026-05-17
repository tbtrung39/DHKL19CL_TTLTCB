def luy_thua(a, n):
    if n == 0:
        return 1
    elif n < 0:
        a = 1 / a
        n = -n
    kq = 1
    for i in range(n):
        kq = kq * a
    return kq
a = input("Nhap a: ")
a = int(a)
n = input("Nhap n: ")
n = int(n)
print("Ket qua:", luy_thua(a, n))
# Giải thích:
# vd nhập a = 2, n = 3 -> luy_thua(2, 3) 
# -> kq = 1 -> i = 0 -> kq = 1*2 = 2 -> i = 1 -> kq = 2*2 = 4 -> i = 2 -> kq = 4*2 = 8 -> return 8
# vd nhập a = 2, n = -3 -> luy_thua(2, -3) 
# -> a = 1/2 = 0.5, n = 3 -> kq = 1 -> i = 0 -> kq = 1*0.5 = 0.5 -> i = 1 -> kq = 0.5*0.5 = 0.25 -> i = 2 -> kq = 0.25*0.5 = 0.125 -> return 0.125    