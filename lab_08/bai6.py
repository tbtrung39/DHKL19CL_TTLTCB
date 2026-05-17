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
def BCNN(a, b):
    return (a * b) // UCLN(a, b)
print("Boi chung nho nhat la:", int(BCNN(a, b)))