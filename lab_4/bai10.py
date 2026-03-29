n = input("Nhập số n: ")
tong = 0
i = 0
while i < len(n):
    if n[i]=='0':
        print("khong" , end=" ")
        tong = tong + 1
    elif n[i]=='1':
        print("mot" , end=" ")
        tong = tong + 1
    elif n[i]=='2':
        print("hai" , end=" ")
        tong = tong + 1
    elif n[i]=='3':
        print("ba" , end=" ")
        tong = tong + 1
    elif n[i]=='4':
        print("bon" , end=" ")
        tong = tong + 1
    elif n[i]=='5':
        print("nam" , end=" ")
        tong = tong + 1
    elif n[i]=='6':
        print("sau" , end=" ")
        tong = tong + 1
    elif n[i]=='7':
        print("bay" , end=" ")
        tong = tong + 1
    elif n[i]=='8':
        print("tam" , end=" ")
        tong = tong + 1
    elif n[i]=='9':
        print("chin" , end=" ")
        tong = tong + 1
    i = i + 1