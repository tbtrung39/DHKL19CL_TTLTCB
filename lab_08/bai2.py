a = input("Nhap vao a: ")
a = int(a)
b = input("Nhap vao b: ")
b = int(b)
def UCLN(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
t = UCLN(a, b)
def value(a,b,t):
    a = a / t
    b = b / t
    print(f'phan so rut gon la:{int(a)}/{int(b)}')
value(a,b,t)