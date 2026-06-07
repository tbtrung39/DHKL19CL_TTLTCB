def pt_b1(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return f"Phương trình có nghiệm x = {x}"
    
def pt_b2(a, b, c):
    if a == 0:
        return pt_b1(b, c)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép x = {x}"
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt x1 = {x1} và x2 = {x2}"