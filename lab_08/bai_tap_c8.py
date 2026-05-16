"""#Bài 7
def tim_max_min(a,b,c):
    so_max=max(a,b,c)
    so_min=min(a,b,c)
    return so_max ,so_min
a= int(input("Nhập số A :"))
b= int(input("Nhập số B :"))
c= int(input("Nhập số C :"))
ln,nn=tim_max_min(a,b,c)
print("Số lớn nhất là :",ln)
print("Số nhỏ nhất là :",nn)

#Bài 8
import math
def tinh_cv(r):
    return 2*math.pi*r
def tinh_dt(r):
    return math.pi *(r**2)
r = float(input("nhập bán kính :"))
if r <0 :
    print("r phải >0")
else:
    chu_vi=tinh_cv(r)
    s=tinh_dt(r)
    print(f"Chu vi hình tròn là :{chu_vi:.2f}")
    print(f"Diện tích hình tròn là :{s:.2f}")
"""
#Bài 9
def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    if a>b:
        return a/b
    else:
        return b/a
a=float(input("nhập a:"))
b= float(input("Nhập b:"))
cong_1=cong(a,b)
tru_1=tru(a,b)
nhan_1=nhan(a,b)
chia_1=chia(a,b)
print(f"kết quả phép cộng là :{cong_1:.2f}")
print(f"kết quả phép trừ là :{tru_1:.2f}")
print(f"kết quả phép nhân là :{nhan_1:.2f}")
print(f"kết quả phép chia là :{chia_1:.2f}")

#Bài 10
def tim_uoc(n):
    ds_u=[]
    for i in range(1,n+1):
        if n%i==0:
            ds_u.append(i)
    return ds_u
n=int(input("nhập n :"))
if n<= 0:
    print("Nhập lại n (n phải >0)")
else:
    cac_u= tim_uoc(n)
    print(f"Các ước số của {n} là :" ,end=' ' )

#Bài 11
def nhap_tt():
    ho_ten=input("Nhập họ tên :")
    toan= float(input("Nhập điểm toán :"))
    ly=float(input("Nhập điểm lý :"))
    hoa= float(input("Nhập điểm hóa :"))
    return {"Họ Tên":ho_ten,"Toán":toan,"Lý":ly,"Hóa":hoa}
def diem_tb(sv):
    diem_tb=(sv["Toán"] +sv["Lý"] +sv["Hóa"])/3
    return diem_tb
svien=nhap_tt()
dtb=diem_tb(svien)
print(f"Họ và tên :{svien['Họ Tên']}, Điểm Toán :{svien['Toán']}, Điểm Lý :{svien['Lý']}, Điểm Hóa :{svien['Hóa']}")

#Bài 12
def tinh_luong_cb(tham_niem):
    luong_goc=5000000
    he_so=1+(tham_niem*0.1)
    return luong_goc*he_so
def nhap_tt_nv():
    ho_ten=input("Nhập họ tên nvien :")
    que_quan=input("Nhập quê quán :")
    tham_nien=int(input("Nhập thâm niên(năm) :"))
    return ho_ten,que_quan,tham_nien
ho_ten,que_quan,tham_nien=nhap_tt()
luong=tinh_luong_cb(tham_nien)
print(f"Họ và tên : {ho_ten}, Quê quán : {que_quan}, Thâm niên :{tham_nien}, Lương :{luong}")

#Bài 13
def ktr_nam_nhuan(y):
    if y%4==0 and y%100!=0 or y%4 ==0:
        return True
    return False
def tinh_so_ngay(m,y):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    elif m==4 or m==6 or m==9 or m==11:
        return 30
    elif m==2:
        if ktr_nam_nhuan(y):
            return 29
        return 28
    else:
        print("Nhập sai nhập lại từ 1->12")

#Bài 14 
n = int(input("nhập số lượng phần tử cho list ;"))
ds=[]
for i in range(n):
    so= int(input(f"Nhập phần tử thứ {i+1} :"))
    ds.append(so)
bp=list(map(lambda x:x ** 2,ds))
print(f"list chứa các bình phương :{bp}")

#Bài 15
n = int(input("nhập số lượng phần tử cho list ;"))
ds=[]
for i in range(n):
    so= int(input(f"Nhập phần tử thứ {i+1} :"))
    ds.append(so)
cac_so_le=filter(lambda x:x%2!=0,ds)
bp_le=list(map(lambda x:x ** 2,ds))
print(f"list chứa các bình phương lẻ :{bp_le}")

#Bài 16
def list_chan():
    ds_list_chan=[]
    for i in range(1,101):
        if i%2==0:
            ds_list_chan.append(i)
    return ds_list_chan
kq=list_chan()
print("Danh sách số chãn [1,100] là :",kq)

#Bài 17
def ktr_chan(x):
    if x%2==0:
        return True
    else:
        return False
def tinh_tong(x, y):
    return x+y
n=int(input("Nhập n :"))
if n<1:
    print("Nhập lại n")
else:
    ds=list(range(1, n+1))
print("Danh sách số là :",ds)
