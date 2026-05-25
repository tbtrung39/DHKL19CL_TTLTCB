def is_tamgiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print(" La tam giac.")
        return True
    else:
        print(" Khong phai la tam giac.")
        return False
def chuvi(a, b, c):
    return print(a + b + c)
def dientich(a, b, c):
    p = (a + b + c) / 2
    return print((p * (p - a) * (p - b) * (p - c)) ** 0.5)