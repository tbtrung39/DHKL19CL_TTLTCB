from datetime import date, timedelta


def next_day(d,m,y):
    try:
        dt=date(y,m,d)
    except Exception as e:
        raise
    nd=dt+timedelta(days=1)
    return nd.day, nd.month, nd.year


def main():
    d=int(input('d: ')); m=int(input('m: ')); y=int(input('y: '))
    nd=next_day(d,m,y)
    print('Ngày kế:', f"{nd[0]:02d}-{nd[1]:02d}-{nd[2]}")

if __name__=='__main__':
    main()
