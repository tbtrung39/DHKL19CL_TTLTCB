from datetime import datetime


def diff_ymd(d1,m1,y1,d2,m2,y2):
    a=datetime(y1,m1,d1)
    b=datetime(y2,m2,d2)
    if a>b:
        a,b=b,a
    days=(b-a).days
    # approximate years and months using calendar months
    y=a.year; m=a.month; day=a.day
    yr=b.year - a.year
    mon=b.month - a.month
    if b.day < a.day:
        mon -=1
    if mon<0:
        yr-=1
        mon+=12
    # remaining days
    tmp = a.replace(year=a.year+yr, month=((a.month+mon-1)%12)+1)
    dd=(b-tmp).days
    return yr, mon, dd


def main():
    d1=int(input('d1: ')); m1=int(input('m1: ')); y1=int(input('y1: '))
    d2=int(input('d2: ')); m2=int(input('m2: ')); y2=int(input('y2: '))
    y,m,d=diff_ymd(d1,m1,y1,d2,m2,y2)
    print(f'Khoảng cách: {y} năm, {m} tháng, {d} ngày')

if __name__=='__main__':
    main()
