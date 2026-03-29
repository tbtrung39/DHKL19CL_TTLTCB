import os
print("menu")
while True:
    print("[1] cafe")
    print("[2] cam vat")
    print("[3] nuoc ep ca rot")
    print("[4] nuoc loc")
    print("[5] nuoc dua")
    print("[0] thoat")

    chon = int(input("chon: "))
    if chon == 1:
        print("ban da chon cafe")
    elif chon == 2:
        print("ban da chon cam vat")
    elif chon == 3:
        print("ban da chon nuoc ep ca rot")
    elif chon == 4:
        print("ban da chon nuoc loc")
    elif chon == 5:
        print("ban da chon nuoc dua")
    elif chon == 0:
        print("thoat")
        break
    else:
        os.system("cls")
    