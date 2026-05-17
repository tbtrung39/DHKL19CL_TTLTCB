def cong(a, b):
    return a + b
def tru(a, b):
    return a - b
def nhan(a, b):
    return a * b
def chia(a, b):
    return a / b
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Cộng: ", cong(a, b))
print("Trừ: ", tru(a, b))
print("Nhân: ", nhan(a, b))
print("Chia: ", chia(a, b))