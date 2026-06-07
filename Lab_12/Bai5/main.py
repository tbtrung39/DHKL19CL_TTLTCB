import sys

def S1(n):
    if n<1:
        raise ValueError('n phải >=1')
    if n==1:
        return 1
    return n+S1(n-1)

def S2(n):
    if n<1:
        raise ValueError('n phải >=1')
    if n==1:
        return 1
    return n*n + S2(n-1)

def main():
    try:
        n=int(input('n: '))
    except:
        print('n không hợp lệ')
        return
    try:
        print('S1=',S1(n))
        print('S2=',S2(n))
    except Exception as e:
        print('Lỗi:',e)

if __name__=='__main__':
    main()
