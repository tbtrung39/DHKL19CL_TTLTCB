list = []
while True :
    x = int(input("nhap so (0 == stop): "))
    if x ==0:
        break
    list.append(x)

#1
list.sort(key=lambda x:x <= 0)
print(list)
            
#2
m = int(input('nhap so m: '))  
list.insert(0 , m )
list.append(m)
list.insert(5,m)
print(list)     