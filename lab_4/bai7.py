a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a>b:
    x=a
else:
    x=b
while True:
    if x%a==0 and x%b==0:
        print("Bội chung nhỏ nhất của",a,"và",b,"là:",x)
        break
    x+=1