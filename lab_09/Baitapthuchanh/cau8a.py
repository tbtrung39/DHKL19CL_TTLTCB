def S(n):
    if n == 1:
        return 1 / (1 * 2)
    S_moi = S(n - 1) + 1 / (n * (n + 1))
    return S_moi

n = input("Nhap n: ")
n = int(n)
S = S(n)
print("S =", S)
# Giải thích:
# vd nhập n = 3 -> S(3) 
# -> S(2) + 1/(3*4) 
# -> S(1) + 1/(2*3) + 1/(3*4) 
# -> 1/(1*2) + 1/(2*3) + 1/(3*4) 
# -> return 0.75
# print("S =", 0.75)