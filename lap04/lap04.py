import math

def cau7():
    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))
    bcnn = (a * b) // math.gcd(a, b)
    print(f"Boi chung nho nhat: {bcnn}")

def cau8():
    char = input("Nhap 1 ky tu bat ky: ")
    print(f"Gia tri ASCII cua '{char}' la: {ord(char)}")

def cau9():
    n = int(input("Nhap vao mot so nguyen duong: "))
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    print(f"Tong cac chu so la: {tong}")

def cau10():
    chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
    n = input("Nhap so nguyen: ")
    ket_qua = ""

    for ky_tu in n:
        if ky_tu == "-":
            ket_qua += "am "
        else:
            ket_qua += chu_so[int(ky_tu)] + " "

    print("Ket qua:", ket_qua.strip())

def cau11():
    menu = ["Cafe", "Cam vat", "Nuoc ep ca rot", "Nuoc loc", "Nuoc dua"]
    don_hang = []

    while True:
        print("\n--- MENU ---")
        print("1. Cafe | 2. Cam vat | 3. Nuoc ep | 4. Nuoc loc | 5. Nuoc dua | 0. Thoat")
        chon = int(input("Chon mon (0-5): "))

        if chon == 0:
            break
        elif 1 <= chon <= 5:
            mon = menu[chon - 1]
            don_hang.append(mon)
            print(f"=> Da them: {mon}")
        else:
            print("Chon sai, vui long chon lai!")

    print("\n--- TONG KET ---")
    if not don_hang:
        print("Chua co mon nao.")
    else:
        for mon in don_hang:
            print("-", mon)

cau7()
cau8()
cau9()
cau10()
cau11()
