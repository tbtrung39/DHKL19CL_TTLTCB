import math

def giaipt_bac1(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    return f"Nghiệm x = {-b/a}"

def giaipt_bac2(a, b, c):
    if a == 0:
        return giaipt_bac1(b, c)
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        return f"Phương trình có nghiệm kép: x = {-b / (2*a)}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
