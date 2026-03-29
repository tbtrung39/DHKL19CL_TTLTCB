# Bai tap tuan 4:
# Bài 7
n= int(input("Nhập số nguyên thứ nhất :"))
m= int(input("Nhập số nguyên thứ hai :"))
bcnn = n 
while bcnn % m !=0  :
    bcnn += n
print("BCNN là :",bcnn)  
#===============================
# Bài 8
while True:
    t = input("Nhập 1 kí tự :")
    if len (t)==1:
        print(f"Mã ASCII của {t} là :",ord(t))
        break
    else:
        print("Vui lòng nhập đúng 1 kí tự !")
#===============================
# Bài 9
n = int(input("Nhập 1 số :"))
tong=0
while n >0 :
    so=n%10
    tong+=so
    n=n//10
print("Tổng các chữ số trong số đó là :",tong) 
#===============================
# Bài 10
n = input("Nhập số thập phân :")
for so in n :
    if so == "1":
        print("mot",end=" ")
    elif so=="2":
        print("hai",end=" ")
    elif so=="3":
        print("ba",end=" ")
    elif so=="4":
        print("bon",end=" ")
    elif so=="5":
        print("nam",end=" ")
    elif so=="6":
        print("sau",end=" ")
    elif so=="7":
        print("bay",end=" ")
    elif so=="8":
        print("tam",end=" ")
    elif so=="9":
        print("chin",end=" ")
    elif so=="0":
        print("khong",end=" ")
    elif so==".":
        print("phay",end=" ")
#===============================
# Bài 11
def menu():
    print("__________MENU__________")
    print("|     1. Cafe            |")
    print("|     2. Cam vắt         |")
    print("|     3. Nước ép cà rốt  |")
    print("|     4. Nước lọc        |")
    print("|     5. Nước dừa        |")
while True:
    menu()
    chon= int(input("Chọn đồ uống :"))
    if chon== 1:
        print("Đã chọn Cafe !")
        break
    elif chon== 2:
        print("Đã chọn Cam vắt !")
        break
    elif chon== 3:
        print("Đã chọn Nước ép cà rốt !")
        break
    elif chon== 4:
        print("Đã chọn Nước lọc !")
        break
    elif chon== 5:
        print("Đã chọn Nước dừa !")
        break
    else:
        print("Chọn lại !")
