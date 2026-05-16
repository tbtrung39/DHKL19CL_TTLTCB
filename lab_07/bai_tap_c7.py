#Bai 1
set_1=set()
while True :
    phan_tu= input("Nhập ký tự (Nhập ESC để kết thúc) :")
    if phan_tu=="ESC":
        break
    if len(phan_tu)>0:
        phan_tu1=phan_tu[0]
        set_1.add(phan_tu1)
kq_xoa=set()
for i in set_1:
    if not i.isdigit():
        kq_xoa.add(i)
set_1=kq_xoa
print("các kí tự sau khi đã xóa là:",set_1)

#Bài 2
n= input("Nhập một chuỗi kí tự số cách nhau bởi dấu cách :").split()
numbers = []
for i in n :
    if i.isdigit():
        so_nguyen=int(i)
        numbers.append(so_nguyen)
a= set()
for so in numbers:
    a.add(so)
print("Tập hợp A từ danh sách Numbers là :" ,a)

#Bài 3
import random 
n = int(input("Nhập số lượng phần tử :"))
a= set()
while len(a)<n:
    so=round(random.uniform(1.0,100.0),2)
    a.add(so)
print("Tập A được sinh ra ngẫu nhiên là :",a)
if a:
    nn=min(a)
    ln=max(a)
    tong=sum(a)
    print(f"Số nhỏ nhất của tập hợp A là :{nn}")
    print(f"Số lớn nhất của tập hợp A là :{ln}")
    print(f"Tổng của tập hợp A là :{tong}")

#Bài 4
chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
#a
so_luong_sv=len(chieu_cao)
print("Số lượng sinh viên là :",so_luong_sv)
#b
chieu_cao_tb= sum(chieu_cao)/so_luong_sv
print(f"Chiều cao trug bình của sinh viên là : {chieu_cao_tb:.2f}")
#c
nhom_chieu_cao=[]
for h in chieu_cao:
    if h not in nhom_chieu_cao:
        nhom_chieu_cao.append(h)
print("Nhóm các chiều cao khác nhau là :",nhom_chieu_cao)
tong_tb=0
for t in nhom_chieu_cao:
    tong_tb=tong_tb+t
nhom_chieu_cao_tb=tong_tb/len(nhom_chieu_cao)
print(f"Chiều cao trung bình của từng nhóm là : {nhom_chieu_cao_tb:.2f} cm")

#Bài 5
import random 
danh_sach=[0,1,2,3,4,5,6,7,8,9]
a= set()
while len(a)<5:
    ptu_ngau_nhien=random.choice(danh_sach)
    a.add(ptu_ngau_nhien)
print("Tập hợp A lad :",a)

#Bài 6
n = int(input("Nhập 1 số tự nhiên n :"))
ds_so_nt_dt=[]
so_kt=2
while len(ds_so_nt_dt)<n :
    la_so_nt= True
    for i in range(2,so_kt):
        if so_kt%i ==0:
            la_so_nt= False
            break
    if la_so_nt== True:
        ds_so_nt_dt.append(so_kt)
    so_kt+=1
print("Dãy n số ngto đầu tiên là :",ds_so_nt_dt)

#Bài 7
import random 
chuoi= input("Nhập một chuỗi kí tự bất kì cả chữ và số :")
ds_ki_tu=list(chuoi)
a= set()
b= set()
if len(ds_ki_tu)>=3:
    while len(a)<4:
        a.add(random.choice(ds_ki_tu))
    while len(b)<4:
        b.add(random.choice(ds_ki_tu))
print("Phần tử A là :",a)
print("Phần tử B là :",b)
phan_tu_chung=set()
for i in a:
    if i in b:
        phan_tu_chung.add(i)
print("Các phần tử chung của A và B là :",phan_tu_chung)

#Bài 8
a={14,3.45,"Phim",78,"hello","Truyền hình",9.0,1}
so_nguyen=0
so_thuc=0
chuoi=0
for i in a:
    if type(i)==int:
        so_nguyen+=1
    elif type(i)== float:
        so_thuc+=1
    elif type== str:
        chuoi+=1
print("Số nguyên trong tập A là :",so_nguyen)
print("Số thực trong tập A là :",so_thuc)
print("Chuỗi trong tập A là :",chuoi)

#Bài 9
n =int(input("Nhập số tự nhiên n :"))
a= set()
b=set()
for i in range(2,n+1):
    kt=True
    for j in range (2,i):
        if i%j==0:
            kt=False
            break
if kt==True:
    if n%i==0:
        a.add(i)
    elif i<n :
        b.add(i)
print("Tập A các số nto là ước của n là :",a)
print("Tập B các số nto < n và ko là ước của n là  :",b)

#Bài 10
n = input("Nhập số n :")
m = input("Nhập số m :")
set_n=set(n)
set_m=set(m)
chu_so_chung=set()
for i in set_m:
    if i in set_n:
        chu_so_chung.add(i)
tong_chu_so=0
for j in chu_so_chung:
    tong_chu_so=tong_chu_so+int(j)
print("Tổng các chữ số chung = ",tong_chu_so )

#Bài 11
c={1,2,3,4,5,6,16}
python={2,4,6,8,9,10,15}
java={1,3,4,5,7,8,15,16}
tat_ca_sv=set()
for sv in c :
    tat_ca_sv.add(sv)
for sv in python :
    tat_ca_sv.add(sv)
for sv in java :
    tat_ca_sv.add(sv)
thi_1_mon=set()
for sv in tat_ca_sv :
    so_mon_thi=0
    if sv in c :
        so_mon_thi+=1
    if sv in python :
        so_mon_thi+=1   
    if sv in java :
        so_mon_thi+=1
    if so_mon_thi==1:
        thi_1_mon.add(sv)
print("Danh sách chỉ thi đúng 1 môn là :",thi_1_mon)
thi_2_mon=set()
for sv in tat_ca_sv:
    if (sv in c and sv in python) or (sv in c and sv in java) or (sv in java and sv in python):
        thi_2_mon.add(sv)
print("Danh sách chỉ thi đúng 2 môn là :",thi_2_mon)
thi_3_mon=set()
for sv in tat_ca_sv:
    if (sv in c) and (sv in python) and (sv in java) :
        thi_3_mon.add(sv)
print("Danh sách chỉ thi đúng 3 môn là :",thi_3_mon)

#Bài 12
n= int(input("Nhập số nguyên n :"))
binh_phuong={}
for i in range (1,n+1):
    gtri_bp=i*i
    binh_phuong[i]=gtri_bp
print("dict đó là :",binh_phuong)

#Bài 13
w=input("Nhập 1 chuỗi kí tự lớn W:")
k=input("Nhập 1 chuỗi kí tự con K cần đếm số lần xuất hiện :")
dem_xh={}
so_lan_xh=0
dd_W=len(w)
dd_K=len(k)
vi_tri=0
while vi_tri<= (dd_W-dd_K):
    chuoi_cat_thu=w[vi_tri:vi_tri+dd_K]
    if chuoi_cat_thu==k:
        so_lan_xh+=1
        vi_tri+=dd_K
    else:
        vi_tri+=1
dem_xh[k]=so_lan_xh
print("kết quả là :",dem_xh)

#Bài 14
nhi_phan={}
for i in range(1,101):
    so_tam=i
    chuoi_nhi_phan=""
    while so_tam>0:
        phan_du=so_tam%2
        chuoi_nhi_phan=str(phan_du)+chuoi_nhi_phan
        so_tam=so_tam//2
    nhi_phan[i]=chuoi_nhi_phan
for j in range(1,11):
    print(f"{k} :'{nhi_phan[k]}'")

#Bài 15 (n=3)
list1=[101,102,103]
list2=["Nguyễn Văn A","Lê Thị B","Trần Văn C"]
tu_dien_sv={}
n= len(list1)
for i in range(0,n):
    khoa=list1[i]
    gtri=list2[i]
    tu_dien_sv=gtri
print("Nội dung của từ điển thu được là :",tu_dien_sv)

#Bài 16
n=int(input("Nhập n :"))
a=[]
for i in range(0,n):
    so=int(input(f"Nhập phần tử thứ {k+1} :"))
    a.append(so)
ktr=False
for j in range(0,n):
    for k in range(j+1,n):
        if a[j]+1==a[k]:
            print(f"({j+1},{k+1})")
            ktr=True
if ktr== False:
    print("Không có cặp chỉ số nào thỏa mãn ĐK")

#Bài 17
du_lieu_sv={}
n=int(input("Nhập số liệu sinh viên :"))
for i in range(n):
    while True:
        ma_sv=input("nhập mã sinh viên (6 kí tự số):")
        if len(ma_sv)==6 and ma_sv.isdigit():
            break
    ten_sv=input("Nhập tên sinh viên :")
    while True :
        diem_sv=int(input("Nhập điểm số từ 0->10 :"))
        if 0<= diem_sv<=10:
            break
        print("Điểm số phải trong khoảng 0->10")
    du_lieu_sv[ma_sv]=[ten_sv,diem_sv]
for j in range (10,-1,-1):
    for ma_sv in du_lieu_sv:
        thong_tin=du_lieu_sv[ma_sv]
        ten_sv=thong_tin[0]
        diem_sv=thong_tin[1]
        if diem_sv==j:
            print(f"Mã sv:{ma_sv} , Tên sv:{ten_sv} , Điểm sv:{diem_sv}")

#Bài 18
tu_dien_thi_sinh = {}

sbd=input("Nhập số báo danh tra cứu điểm :")
if sbd in tu_dien_thi_sinh:
    thong_tin=tu_dien_thi_sinh[sbd]
    print(f"Họ và tên : {thong_tin[0]}, Điểm thi :{thong_tin[1]}")
else:
    print("Không tìm thấy vui lòng nhập thông tin mới")
    ten_moi=input("Nhập tên sv:")
    diem_moi=float(input("Nhập điểm:"))
    tu_dien_thi_sinh[sbd]=[ten_moi,diem_moi]
    print("Đã nhập thông tin mới !")

#Bài 19
#a
n= int(input("Nhập số lượng cần nhập :"))
tu_dien_nv = {}
for i in range (0,n):
    while True:
        ma_nv=int(input(f"Nhập mã nvien thứ {i+1} (4 chữ số):"))
        if len(ma_nv)==4:
            break
        ten_nv=input(f"Nhập tên nhân viên thứ {i+1}:")
        while len(ten_nv)<20:
            ten_nv=ten_nv+" "
        ten_nv=ten_nv[0:20]
        nam_sinh= int(input("Nhập năm sinh :"))
        luong=int(input("Nhập mức lương :"))
        tu_dien_nv[ma_nv]=[ten_nv,nam_sinh,luong]
#b
while True:
    ma_nv_moi=input("Nhập mã nhân viên mới (4 chữ số):")
    if len(ma_nv_moi)==4:
            break
    ten_nv_moi=input("Nhập tên nhân viên:")
    while len(ten_nv_moi)<20:
            ten_nv_moi=ten_nv_moi+" "
            ten_nv_moi=ten_nv_moi[0:20]
            nam_sinh_moi= int(input("Nhập năm sinh :"))
            luong_moi=int(input("Nhập mức lương :"))
            tu_dien_nv[ma_nv_moi]=[ten_nv_moi,nam_sinh_moi,luong_moi]
            print("Đã thêm vào danh sách nv mới")
#c
x=input("Nhập mã nhân viên x :")
if x in tu_dien_nv:
    nv=tu_dien_nv[x]
    print(f"Tìm thấy Tên :{nv[0]}, Năm sinh {nv[1]}, Lương :{nv[2]}")
else:
    print("Không tìm thấy ")
#d
y = input("Nhập mã nhân viên :")
if y in tu_dien_nv:
    tu_dien_nv[y][2]=tu_dien_nv[y]+1000000
    print("Đã tăng lương cho nhân viên")
else:
    print("Không tìm thấy nhân viên")
#e
z = input("Nhập mã nhân viên :")
if z in tu_dien_nv:
    del tu_dien_nv[z]
    print("Đã xóa nhân viên !")
else:
    print("Không tìm thấy nhân viên")
#f
ds=[]
for ma in tu_dien_nv:
    ds.append([ma,tu_dien_nv[ma]])
m=len(ds)
for i in range(0,m):
    for j in range(i+1,m):
        nam_sinh_i=ds[i][1][1]
        nam_sinh_j=ds[j][1][1]
        if nam_sinh_i<nam_sinh_j:
            bien=ds[i]
            ds[i]=ds[j]
            ds[j]=bien
for k in ds:
    ma_nv_sx=k[0]
    ten_nv_sx=k[1][0]
    nam_sinh_sx=k[1][1]
    luong_sx=k[1][2]
    print(f"Mã :{ma_nv_sx} ,Tên :{ten_nv_sx}, Năm sinh {nam_sinh_sx}, Lương :{luong_sx}")