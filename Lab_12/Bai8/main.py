from datetime import date, timedelta


def prev_day(d,m,y):
    dt=date(y,m,d)
    pd=dt-timedelta(days=1)
    return pd.day, pd.month, pd.year


def main():
    d=int(input('d: ')); m=int(input('m: ')); y=int(input('y: '))
    pd=prev_day(d,m,y)
    print('Ngày trước:', f"{pd[0]:02d}-{pd[1]:02d}-{pd[2]}")

if __name__=='__main__':
    main()
