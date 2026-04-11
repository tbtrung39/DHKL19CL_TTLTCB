list = []
while True :
    x = int(input("nhap so (0 == stop): "))
    if x ==0:
        break
    list.append(x)

#1
list.insert(0,[1,2,3])
list.append([1,2,3])
list.insert(5,[1,2,3])
print(list)

#2
k = int(input('nhap k: '))
list.pop(k-1)
print(list)

#3
tang = sorted(list)
giam = sorted(list , reverse=True)
print(tang)
print(giam)