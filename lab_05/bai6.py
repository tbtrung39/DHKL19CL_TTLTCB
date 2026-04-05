str = input(" nhap chuoi: ").upper()
HEX='0123456789ABCDEF'

hop_le = True
for char in str:
    if char not in HEX:
        hop_le = False
        break

if hop_le:
    print(f" Chuoi la HEX hop le ")
    print(f" Chuoi sau khi chuyen sang thap phan: {int(str, 16)}")

else:
    print(f" Chuoi khong phai la HEX hop le ")

    so_hex=""
    for char in str:
        if char in HEX:
            so_hex+=char
    print(f" Chuoi sau khi loai bo ky tu khong phai HEX: {so_hex} ")

    if so_hex!="":
        print(f" Chuoi sau khi chuyen sang thap phan: {int(so_hex, 16)}")
    else:
        print(f" Khong co ki tu hop le")