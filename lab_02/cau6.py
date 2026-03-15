n = int(input('nhap so nguyen co 3 chu so: '))
if n<100:
    print('nhap lai')
don_vi = n %10
chuc= (n//10)%10
tram = n //100
so_doc = ['khong','mot','hai','ba','bon','nam','sau','bay','tam','chin']
print(so_doc[tram],'tram',so_doc[chuc],'muoi',so_doc[don_vi] )
