#7
a = int(input('nhap a: '))
b = int(input('nhap b: '))

if a <= 0 or b <= 0:
    print('moi ban nhap lai')
else:
    i = max(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            print('BCNN la:', i)
            break
        i += 1
#8
ch = input("Nhập ký tự: ")
i = 0
while i < len(ch):
    print("ASCII của", ch[i], "là:", ord(ch[i]))
    i += 1
#9
n = int(input('moi ban nhap so: '))
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print('tong cac chu so la:', tong)
#10
n = int(input('moi nhap so: '))
chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
ket_qua = ""
while n > 0:
    ket_qua = chu_so[n % 10] + " " + ket_qua
    n //= 10
print("doc la:", ket_qua.strip())
if n == 0:
    print("khong")
#11
while True:
    print('\n menu')
    print('1.Cafe')
    print('2.Cam vat')
    print('3.Nuoc ep ca rot')
    print('4.Nuoc loc')
    print('5.Nuoc dua')
    print('0.Thoat')
    chon = int(input('moi ban chon: '))
    if chon == 1:
        print('cafe')
    elif chon == 2:
        print('cam vat')
    elif chon == 3:
        print('nuoc ep ca rot')
    elif chon == 4:
        print('nuoc loc')
    elif chon == 5:
        print('nuoc dua')
    elif chon == 0:
        print('thoat')
        break
    else:
        print('lua chon khong hop le')