a = input("Nhap so a: ")
a = int(a)
b = input("Nhap so b: ")
b = int(b)
c = input("Nhap so c: ")
c = int(c)
def min(a,b,c):
    min = a
    if b < min:
        min = b
    elif c < min:
        min = c
    print(f"min = {min}")
def max(a,b,c):
    max = a
    if b > max:
        max = b
    elif c > max:
        max = c
    print(f"max = {max}")
min(a,b,c)
max(a,b,c)