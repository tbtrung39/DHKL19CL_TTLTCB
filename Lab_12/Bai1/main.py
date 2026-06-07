import math


def area_triangle(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))


def main():
    try:
        a=float(input('a: '))
        b=float(input('b: '))
        c=float(input('c: '))
    except Exception:
        print('Lỗi: a,b hoặc c không phải là số')
        return
    if a<=0 or b<=0 or c<=0:
        print('Lỗi: cạnh phải dương')
        return
    if not (a+b>c and a+c>b and b+c>a):
        print('Lỗi: không phải ba cạnh tam giác')
        return
    print('Diện tích:', area_triangle(a,b,c))

if __name__=='__main__':
    main()
