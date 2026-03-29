#7
import math
a = int(input("nhap so thu 1: "))
b = int(input("nhap so thu 2: "))
ucln = math.gcd(a, b)
bcnn = abs(a * b) // ucln
print(f"boi chung nho nhat cua {a} va {b} la: {bcnn}")

#8
ky_tu = input("nhap 1 ky tu bat ky: ")

if len(ky_tu) > 0:
    char = ky_tu[0]
    ma_ascii = ord(char)
    print(f"gia tri ASCII cua ky tu '{char}' la: {ma_ascii}")
else:
    print("Chua nhap ky tu nao!")

#9
n_goc = int(input("Nhap vao mot so nguyen duong: "))
n = abs(n_goc) 
tong = 0
while n > 0:
    chu_so = n % 10  
    tong += chu_so    
    n = n // 10     
print(f"tong cac chu so cua {n_goc} la: {tong}")

#10
chu_so = ["khong","mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]

n = int(input("nhap so nguyen: "))
n_temp = abs(n) 
ket_qua = []

if n_temp == 0:
    ket_qua.append(chu_so[0])
else:
    while n_temp > 0:
        don_vi = n_temp % 10         
        ket_qua.append(chu_so[don_vi]) 
        n_temp //= 10                
ket_qua.reverse()
if n < 0:
    ket_qua.insert(0, "am")

print("ket qua:", " ".join(ket_qua))
#11
def menu_do_uong():
    print("----- MENU DO UONG -----")
    print("1. Cafe")
    print("2. Cam vat")
    print("3. Nuoc ep ca rot")
    print("4. Nuoc loc")
    print("5. Nuoc dua")
    print("0. Thoat chuong trinh")
    print("------------------------")
don_hang = []
while True:
    menu_do_uong()
    try:
        lua_chon = int(input("chon so (1-5): "))
    except ValueError:
        print("nhap chu so")
        continue
    if lua_chon == 1:
        mon = "Cafe"
    elif lua_chon == 2:
        mon = "Cam vat"
    elif lua_chon == 3:
        mon = "Nuoc ep ca rot"
    elif lua_chon == 4:
        mon = "Nuoc loc"
    elif lua_chon == 5:
        mon = "Nuoc dua"
    elif lua_chon == 0:
        print("ok!")
        break
    else:
        print("Khong co,chon lai.")
        continue

    print(f"==> da chon: {mon}")
    don_hang.append(mon)
    tiep_tuc = input("muon đat them mon khac khong? (c/k): ").lower()
    if tiep_tuc != 'c':
        break
print("\n" + "="*25)
print("TONG KET DON HANG:")
if not don_hang:
    print("Chua co mon nao duoc chon.")
else:
    for i, m in enumerate(don_hang, 1):
        print(f"{i}. {m}")
print("="*25)
print("Hen gap lai !")