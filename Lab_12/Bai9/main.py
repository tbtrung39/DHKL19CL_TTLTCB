import datetime


def main():
    d=int(input('d: ')); m=int(input('m: ')); y=int(input('y: '))
    dt=datetime.date(y,m,d)
    # week number in year
    week=dt.isocalendar()[1]
    print('Thuộc tuần thứ:', week)

if __name__=='__main__':
    main()
