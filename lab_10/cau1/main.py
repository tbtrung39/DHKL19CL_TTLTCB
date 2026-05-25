import my_Traiage
a = input("Nhap canh a: ")
a = float(a)
b = input("Nhap canh b: ")
b = float(b)
c = input("Nhap canh c: ")
c = float(c)
if my_Traiage.is_tamgiac(a, b, c):
    my_Traiage.chuvi(a, b, c)
    my_Traiage.dientich(a, b, c)
else:
    print("Nhap lai")