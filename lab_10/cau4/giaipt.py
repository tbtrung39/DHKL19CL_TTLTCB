import math
def pt_bn_mot_an(a,b):
    x = -b/a
    return print("x =",x)
def pt_bn_hai_an(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return print("PT vo nghiem")
    elif delta == 0:
        x = -b/(2*a)
        return print("PT co nghiem kep x =",x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return print("PT co hai nghiem phan biet x1 =",x1,"va x2 =",x2)