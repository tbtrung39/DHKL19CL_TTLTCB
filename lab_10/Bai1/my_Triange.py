def is_TamGiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
    
def chuVi(a, b, c):
    return a + b + c

def S_TamGiac(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5