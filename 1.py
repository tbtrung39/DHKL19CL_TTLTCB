canh=[]
ten_canh = ['a','b','c']
for ten in ten_canh:
    while True:
        try:
            gia_tri = float(input(f"Nhap canh {ten}: "))
            if gia_tri<=0:
                print('vui long nhap lai')
                continue
            canh.append(gia_tri)
            break
        except ValueError:
            print('vui long nhap so ')

a , b ,b = canh[0],canh[1],canh[2]
if a+b<=c or a+c<=b or b+c <=a:
    print('3 canh ko tao thanh 1 tam giac')
else:
    p= (a+b+c)/2
    s =(p*(p-a)*(p-b)*(p-c))**(1/2)
    print(f"3 canh: {a} , {b}, {c}")
    print(s)
