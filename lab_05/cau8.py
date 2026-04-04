str =input('nhap doan van: ')
tu  = input('nhap tu can tim: ')
dem = 0
chu = ""

for i in str:
    if i != " ":
        chu = chu +i
    else:
        if chu == tu:
            dem = dem +1
        chu = ""

if chu == tu:
    dem = dem +1

print('Tu', tu ,'xuat hien ', dem ,'lan' )