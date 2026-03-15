thang = int(input('nhap thang: '))
if thang ==2:
    print(f'thang 2 có 28day or 29day(nhuan)')
elif thang % 2==0:
    print(f'thang {thang} có 30day')
else:
    print(f'thang {thang} có 31 day')