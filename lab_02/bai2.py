import math
a, b, c = map(float, input("Nhap 3 so: ").split())

def giai_pt_bac_2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phuong trinh co vo so nghiem"
            else:
                return "Phuong trinh vo nghiem"
        else:
            return f"Phuong trinh co mot nghiem duy nhat: x = {-c/b}"
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phuong trinh vo nghiem"
        elif delta == 0:
            return f"Phuong trinh co nghiem kep: x = {-b/(2*a)}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}"

result = giai_pt_bac_2(a, b, c)
print(result)