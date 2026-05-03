#a
def namnhuan(y):
    if y%400==0 or (y%4==0 and y%100!=0):
        return True
    return False

#b
def songay(thang, nam):
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        if namnhuan(nam):
            return 29
        else:
            return 28

m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))

print("So ngay:", songay(m,y))