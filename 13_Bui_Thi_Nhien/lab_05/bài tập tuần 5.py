#Bài 5
s = input("Nhạp chuỗi :")
kq= ""
for ch in s:
    if ch.isdigit():
        kq+=ch
print("Chuỗi sau khi xóa là :",kq)

#Bài 6
s = input("Nhập chuỗi :")
ktra= True
dem_cham=0
for i in range (len(s)):
    if s[i]=='.':
        dem_cham+=1
        if dem_cham>1:
            ktra= False
    elif s[i] in '+-':
        if i != 0 :
            ktra= False
    elif not s[i].isdigit():
        ktra= False
if s in ['+','-','.','+.','-.']:
    kta= False
if ktra:
    print("Là số hệ thập phân")
else:
    print("Không phải số hệ thập phân")

#Bài 7
s= input("Nhập chuỗi :")
so=""
for ch in s:
    if ch.isdigit():
        so+= ch
if so == so[::-1]:
    print("Chuỗi số đối xứng")
else:
    print("Chuỗi số không đối xứng")

#Bài 8
s= input("Nhập chuỗi :")
kq= s.title()
print("Chuỗi sau khi chuẩn hóa :",kq)

#Bài 9
s= input("Nhập chuỗi :")
so_ki_tu= len(s)
so_tu= len(s.split())
print("Số kí tự là :", so_ki_tu)
print("Số từ là :",so_tu)

#Bài 10
s1= input("Nhập chuỗi 1 :")
s2= input("Nhập chuỗi 2 :")

list1= s1.split()
list2= s2.split()
dem=0
for tu in list1 :
    if tu in list2:
        dem+=1
print("Số từ giống nhau :", dem)

#Bài 11
s= input("Nhập chuỗi nhị phân :")
kq=0
t=0
for i in range(len(s)-1,-1,-1):
    if s[i]== '1':
        kq += 2**t
    t+=1
print("Số thập phân là :",kq)

#Bài 12
s=input("Nhập chuỗi :")
dem=0
ktra=False
for ch in s:
    if ch!= ' ':
        if not ktra :
            dem+=1
            kta= True
    else:
        ktra= False
print("Số từ là :",dem)

#Bài 13
A= input("Nhập chuỗi A :")
B= input("Nhập chuỗi B :")
soA=""
soB=""
for ch in A :
    if ch.isdigit():
        soA+= ch
for ch in B :
    if ch.isdigit():
        soB+=ch
if soA =="":
    soA= "0"
if soB =="":
    soB="0"
print(soA+"+"+soB)
