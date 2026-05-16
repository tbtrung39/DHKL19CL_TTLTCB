"""#Bài 1
def lon_nhat_3(a,b,c):
    def lon_nhat_2(x,y):
        if x>y:
            return x
        else:
            return y
    return lon_nhat_2(a,lon_nhat_2(b,c))
a= int(input("Nhập a :"))
b= int(input("Nhập b :"))
c= int(input("Nhập c :"))
lon_nhat=lon_nhat_3(a,b,c)
print(f"Số lớn nhất trong 3 số {a},{b},{c} là :{lon_nhat}")

#Bài 2
def ucln(a,b):
    if b==0:
        return a
    return ucln(b,a%b)
def ucln_n_so(m,n):
    if n==1 :
        return m[0]
    return ucln( m[n-1] ,ucln_n_so(m,n-1))
n= int(input("Nhập n :"))
m=[]
for i in range (n):
    x=int(input(f"Nhập phần tử thứ {i+1} :"))
    m.append(x)
kq=ucln_n_so(m,n)
print("UCLN của dãy là :",kq)

#Bài 3
def luy_thua(a,n):
    if n==0:
        return 1
    return a*luy_thua(a,n-1)
a= int(input("Nhập a:"))
n= int(input("Nhập n :"))
kp=luy_thua(a,n)
print("Kết quả là :",kq)

#Bài 4
def hoan_vi(a,b,c):
    if b==c:
        print(a)
    else:
        for i in range(1,c+1):
            a[b]=a[i]
            a[i]=a[b]
            hoan_vi(a,b+1,c)
            a[b]=a[i]
            a[i]=a[b]
n=int(input("Nhập n :"))
a=[]
for i in range(1,n+1):
    a.append(i)
kq=hoan_vi(a,0,n-1)
print("Hoán vị =",kq)

#Bài 5
def permutation(n):
    if n==1:
        return[[1]]
    t=permutation(n-1)
    kq=[]
    for i in t:
        for j in range(len(j)+1):
            k=j.coppy()
            k.insert(j,n)
            kq.append(k)
    return kq
n= int(input("Nhập n :"))
kq_1=permutation(n)
for x in kq_1:
    print(x)

#Bài 6
import random
def hoan_vi_ngau_nhien(a,n):
    if n==1:
        return a
    k=random.randint(0,n-1)
    a[k]=a[n-1]
    a[n-1]=a[k]
    return hoan_vi_ngau_nhien(a,n-1)
n=int(input("Nhập n :"))
a=[]
for i in range(1,n+1):
    a.append(i)
hoan_vi_ngau_nhien(a,n)
print("Hoán vị ngẫu nhiên :",a)

#Bài 7
def tim_nghiem(a,n,tong_con_lai,b):
    if a==n-1:
        b[a]=tong_con_lai
        print(b)
        return
    for i in range (tong_con_lai+1):
        b[a]=i
        tim_nghiem(a+1,n,tong_con_lai-i,b)
n=int(input("Nhập n :"))
N=int(input("Nhập tổng còn lại :"))
b=[0]*n
kq=tim_nghiem(0,n,N,b)

#Bài 8
#a
def tong_a(n):
    if n==1:
        return 1/(1*2)
    return 1/(n*(n+1))+tong_a(n-1)
#b
def mau(n):
    if n==0 or n==1 :
        return 1
    return n*tong_b(n-1)
def tong_b(n):
    if n==1:
        return 1
    return 1/mau(n)+tong_b(n-1)
#c
def tong_c(n):
    if n==1:
        return (3)**0.5
    return (3*n+tong_c(n-1))**0.5
#d
def tong_d(n):
    if n ==1:
        return 1**0.5
    return (n+tong_d(n-1))**(1/(n+1))

#Bài 9
def dao_nguoc(n):
    print(n%10, end =" ")
    if n>=10:
        dao_nguoc(n//10)
n=int(input("Nhập n :"))
kq_2=dao_nguoc(n)
print("Kết quả sau đảo ngược là :",kq_2)

#Bài 10
def x(n):
    if n==0:
        return 1
    tong=0
    for i in range (n):
        tong+=(n-1)**2*x(i)
    return tong
n=int(input("Nhập n :"))
kq_3=x(n)
print("Kết quả là :",kq_3)

#Bài 11
def gt_kep(n):
    if n==0 or n==1:
        return 1
    return n*gt_kep(n-2)
def tinh_s(k):
    tong=0
    for i in range (1,k+1):
        if i%2==1:
            tong+=gt_kep(i)
        else:
            tong-=gt_kep(i)
    return tong
k=int(input("Nhập K :"))
kq_4=tinh_s(k)
print("S=",kq_4)
"""
#Bài 12
def tim_ga_cho(g,c):
    if g+c==36 and 2*g+4*c==100:
        print("Số gà =",g)
        print("Số chó =",c)
        return 
    if g>36:
        return
    tim_ga_cho(g+1,c-1)
tim_ga_cho(0,36)