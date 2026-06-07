def Ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Bscn(a, b):
    return a * b // Ucln(a, b)

def SumDivisor(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum