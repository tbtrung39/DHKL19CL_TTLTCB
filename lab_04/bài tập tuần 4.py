"""# Bài 7
n= int(input("Nhập số nguyên thứ nhất :"))
m= int(input("Nhập số nguyên thứ hai :"))
bcnn = n 
while bcnn % m !=0  :
    bcnn += n
print("BCNN là :",bcnn)  

# Bài 8
while True:
    t = input("Nhập 1 kí tự :")
    if len (t)==1:
        print(f"Mã ASCII của {t} là :",ord(t))
        break
    else:
        print("Vui lòng nhập đúng 1 kí tự !")

# Bài 9
n = int(input("Nhập 1 số :"))
tong=0
while n >0 :
    so=n%10
    tong+=so
    n=n//10
print("Tổng các chữ số trong số đó là :",tong) 

# Bài 10
n = input("Nhập số thập phân :")
for so in n :
    if so == "1":
        print("một",end=" ")
    elif so=="2":
        print("hai",end=" ")
    elif so=="3":
        print("ba",end=" ")
    elif so=="4":
        print("bốn",end=" ")
    elif so=="5":
        print("năm",end=" ")
    elif so=="6":
        print("sáu",end=" ")
    elif so=="7":
        print("bảy",end=" ")
    elif so=="8":
        print("tám",end=" ")
    elif so=="9":
        print("chín",end=" ")
    elif so=="0":
        print("không",end=" ")
    elif so==".":
        print("phẩy",end=" ")
"""
# Bài 11
def menu():
    print("__________MENU__________")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
while True:
    menu()
    chon= int(input("Chọn đồ uống :"))
    if chon== 1:
        print("Bạn đã chọn Cafe !")
        break
    elif chon== 2:
        print("Bạn đã chọn Cam vắt !")
        break
    elif chon== 3:
        print("Bạn đã chọn Nước ép cà rốt !")
        break
    elif chon== 4:
        print("Bạn đã chọn Nước lọc !")
        break
    elif chon== 5:
        print("Bạn đã chọn Nước dừa !")
        break
    else:
        print("Bạn hãy chọn lại !")