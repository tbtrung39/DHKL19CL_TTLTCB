def ucln(a,b):
    while b != 0:
        r = a % b
        a = b  
        b = r
    return print("UCLN =",a)
def bcnn(a,b):
    while b != 0:
        r = a % b
        a = b  
        b = r
    ucln = a
    bcnn = (a * b) / ucln
    return print("BCNN =",bcnn)
def sumdivision(n):
    sumdivision = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sumdivision = sumdivision + i
            print("Tong cac uoc =",sumdivision)
        return sumdivision