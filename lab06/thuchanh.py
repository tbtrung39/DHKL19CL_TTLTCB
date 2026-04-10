# 1. Cho danh sách a = [2,-4,1,9,-3,6,3,-2,6,8] gồm n = 10 phần tử.
# Yêu cầu:
# a. Viết chương chình python tính tổng:
a = [2,-4,1,9,-3,6,3,-2,6,8]
tong = 0
for i in a:
    tong = tong + i
print("Tổng của các phần tử trong danh sách a là:", tong)

# b. Viết chương trình python đếm số lượng các số hạng dương và tổng các số hạng dương:
viet_duong = 0
tong_duong = 0
for i in a:
    if i > 0:
        viet_duong = viet_duong + 1
        tong_duong = tong_duong + i
print("Số lượng các số hạng dương là:", viet_duong)
print("Tổng các số hạng dương là:", tong_duong)
__author__ = "Lê Quốc Việt"
__copyright__ = "Bài tập tuần 6"
__license__ = "MIT"

# c. Tìm vị trí phần tử âm đầu tiên có trong danh sách:
vitri = -1
for i in range(len(a)):
    if a[i] < 0:
        vitri = i
        break
if vitri != -1:
    print("Vị trí phần tử âm đầu tiên trong danh sách a là:", vitri)
else:
    print("Không có phần tử âm nào trong danh sách a.")

# d. Tìm vị trí phần tử dương cuối cùng có trong danh sách:
vitri_duong = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vitri_duong = i
        break
if vitri_duong != -1:
    print("Vị trí phần tử dương cuối cùng trong danh sách a là:", vitri_duong)
else:
    print("Không có phần tử dương nào trong danh sách a.")

# e. Tìm phần tử lớn nhất và vị trí lớn nhất cuối cùng có trong danh sách:
max_value = a[0]
vitri_max = 0
for i in range(1, len(a)):
    if a[i] >= max_value:
        max_value = a[i]
        vitri_max = i
print("Phần tử lớn nhất trong danh sách a là:", max_value)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách a là:", vitri_max)

#============================================
# 2. Nhập từ bàn phím n, trong đó:
# a. Tìm phần tử lớn nhất thứ 32 trong ds và vị trí phần tử lớn nhất đạt vị trí thứ 2:
n = int(input("Nhập số lượng phần tử n: "))
ds = []
for i in range(n):
    vit = int(input("Nhập phần tử thứ {}: ".format(i+1)))
    ds.append(vit)
max_viet = ds[0]
vitri_max = 0
for i in range(1, len(ds)):
    if ds[i] >= max_viet:
        max_viet = ds[i]
        vitri_max = i
print("Phần tử lớn nhất trong danh sách ds là:", max_viet)
print("Vị trí phần tử lớn nhất cuối cùng trong danh sách ds là:", vitri_max)

# b. Tính số lượng các số dương liên tiếp nhiều nhất trong ds:
max_duong = 0
quoc_duong = 0
for i in range(len(ds)):
    if ds[i] > 0:
        quoc_duong = quoc_duong + 1
        if quoc_duong > max_duong:
            max_duong = quoc_duong
    else:
        quoc_duong = 0
print("Số lượng các số dương liên tiếp nhiều nhất trong danh sách ds là:", max_duong)

# c. Tính số lượng số dương liên tiếp có tổng max:
maxTongDuong = 0
tongDuong = 0
for i in range(len(ds)):
    if ds[i] > 0:
        tongDuong = tongDuong + ds[i]
        if tongDuong > maxTongDuong:
            maxTongDuong = tongDuong
    else:
        tongDuong = 0
print("Số lượng số dương liên tiếp có tổng max trong danh sách ds là:", maxTongDuong)

#============================================
# 3. Nhập 1 danh sách phần tử cho đến khi nhập vào số 0, trong đó:
# a. Viết các phần tử dương của ds lên dâdu ds và in ra màn hình:
ds = []
while True:
    quocviet = int(input("Nhập phần tử (nhập 0 để kết thúc): "))
    if quocviet == 0:
        break
    ds.append(quocviet)
print("Danh sách phần tử đã nhập:", ds)

print("Các phần tử dương trong danh sách ds là:")
for i in ds:
    if i > 0:
        print(i)

# b. Chèn m nhập từ bàn phím vào đầu vào cuối và vào vị trí thứ 5:
v = int(input("Nhập số m: "))
ds.insert(0, v)  
ds.append(v)    
if len(ds) >= 5:
    ds.insert(4, v) 
print("Danh sách sau khi chèn m vào đầu, cuối và vị trí thứ 5:", ds)

#============================================
# 4. Nhập 1 danh sách phần tử cho đến khi nhập vào số 0, trong đó:
# a. Chèn [1,2,3] vào đầu, cuối, vitri thứ 5 của ds:
ds = []
while True:
    Quocviet = int(input("Nhập phần tử (nhập 0 để kết thúc): "))
    if Quocviet == 0:
        break
    ds.append(Quocviet) 
ds.insert(0, [1, 2, 3])
ds.append([1, 2, 3])
if len(ds) >= 5:
    ds.insert(4, [1, 2, 3])
print("Danh sách sau khi chèn [1, 2, 3] vào đầu, cuối và vị trí thứ 5:", ds)

# b. Xóa phần tử thứ k nhập từ bàn phím:
k = int(input("Nhập vị trí k để xóa phần tử: "))
if 0 <= k < len(ds):
    xoa = ds.pop(k)
    print("Đã xóa phần tử tại vị trí {}: {}".format(k, xoa))
else:
    print("Vị trí k không hợp lệ.")

# c. Sắp xếp theo thứ tự giảm và tăng:
ds.sort()
print("Danh sách sau khi sắp xếp theo thứ tự tăng:", ds)
ds.sort(reverse=True)
print("Danh sách sau khi sắp xếp theo thứ tự giảm:", ds)

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