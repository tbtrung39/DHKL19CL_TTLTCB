hex_string = "0123456789ABCDEF"
n = input("Nhập mã hex: ")
n = n.upper()
new_hex_str = ""
check = False
for char in n:
    if char in hex_string:
        new_hex_str = new_hex_str + char
        check = True
    else:
        print("Mã hex không hợp lệ.")
        continue
if check == True:
    print("Chuỗi bao gồm ký tự không trong hệ Hex")
print("chuỗi Hex",new_hex_str )
dex = 0
pos = len(new_hex_str) - 1
for char in new_hex_str:
    if char in new_hex_str:
        if char == "A":
            number = 10
        elif char == "B":
            number = 11
        elif char == "C":
            number = 12
        elif char == "D":
            number = 13
        elif char == "E":
            number = 14
        elif char == "F":
            number = 15
        else:
            number = int(char)
        dex = dex + number * (16 ** pos)