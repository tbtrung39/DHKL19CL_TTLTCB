#Bài 5
import random
a= [random.randint(1,99999)
    for i in range(1000)]
print(a)

#Bài 6
a=[random.randint(1,99999)
   for i in range (1000)]
#Cách 1 sd sorted
b= sorted(a)
print("Dùng sorted ():")
print(b)
#Cách 2 không sd sorted
c= a.copy()
for i in range (len(c)):
    for j in range (0,len(c)-i-1):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
print("Không su dung sorted():")
print(c)

#Bài 7
List1 = [["mon", 73], ["tue", 89], ["wed", 95],
         ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách :")
for i in List1:
    print(i)
import random 
print("Độ dài :",len(List1))
new_i=["new_day",random.randint(50,150)]
List1.append(new_i)
print("Sau khi thêm :",List1)
tong=List1[1][1] + List1[2][1] +List1[5][1] +List1[6][1] 
print("Tổng :",tong)

#Bài 8
n= int(input("Nhập n :"))
fib=[0,1]
for i in range (2,n):
    fib.append(fib[i-1]+fib[i-2])
print(",".join(str(x) for x in fib[:n]))

#Bài 9
a= list(map(int,input("Nhập các số cách nhau bằng dấu cách :").split()))
for x in a:
    assert x% 2==0 , "Danh sách có số lẻ!"
print("Tất cả phần tử đều là số chẵn !")

#Bài 10
import random 
a= [x for x in range(201) if x%5==0 and x%7==0]
print(random.choice(a))

#Bài 11
n = int(input("Nhập n :"))
a=[]
for i in range(n):
    x= int(input(f"Nhập phần tử thứ {i+1}:"))
    a.append(x)
#a
b=[x for x in range(201) if x%3 ==0 and x%5!=0]
print(b)
#b
c=[x**2 for x in a]
print(c)
#c
ten = input("Nhập các tên cách nhau bằng dấu cách :").split()
d= [name[0].upper() for name in ten ]
print(d)

#Bài 12
tien_bd =0
while True:
    n = input("Nhập dữ liệu (Nhập ! để kết thúc) :")
    if n =="!":
        break
    a,x =n.split()
    x= int(x)
    if a =='D':
        tien_bd+=x 
    elif a=='W':
        tien_bd-=x
print(tien_bd)

#Bài 13
s=["Anh","Em"]
v=["Chơi","Yêu"]
o=["Bóng đá","Bóng rổ"]
cau=[s1+" "+v1+" "+o1
     for s1 in s
     for v1 in v
     for o1 in o]
for cau1 in cau:
    print(cau1)

#Bài 14
passwords = input("Nhập mâtk khẩu :").split(',')
kq=[]
for i in passwords:
    if 6<= len(i)<=12:
        ktra_chu= False
        ktra_chu_hoa= False
        ktra_so=False
        ktra_kitu=False
        for ch in i:
            if 'a' <= ch <='z':
                ktra_chu= True
            elif 'A' <= ch <='Z':
                ktra_chu_hoa= True 
            elif 'A' <= ch <='Z':
                ktra_so= True 
            elif 'A' <= ch <='Z':
                ktra_kitu= True 
        if ktra_chu and ktra_chu_hoa and ktra_so and ktra_kitu:
            kq.append(i)
print(",".join(kq)) 

#Bài 15
n= input("Nhập :").split(',')
lst=[]
for i in n:
    name, age,score = i.split(':')
    lst.append((name, int(age), int(score)))
lst.sort(key =lambda x :(x[0],x[1],-x[2]))
print(lst)

#Bài 16
x , y = map (int , input("Nhập x , y :").split())
matrix=[[i*j for j in range(y)] for i in range (x)]
print(matrix)

#Bài 17
n= int(input("Nhập n :"))
matrix =[[1 if i==j else 0 for j in range (n)] for i in range (n)]
for r in matrix :
    print(r)

#Bài 18
m,n = map(int,input("Nhập hàng và cốt MxN :").split())
a=[]
for i in range (m):
    r= list(map(int, input("nhập hàng:").split()))
    a.append(r)
print("Ma trận A là :")
for r in a:
    print(r)


tong=0
for r in a:
    for i in range (len(a)):
        for j in range (len(a[i])):
            tong+=a[i][j]
print("Tổng = ",tong)