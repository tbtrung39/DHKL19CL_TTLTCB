str = input('nhap chuoi: ').upper
hex = '0123456789ABCDEF'
la_hex = True
for i in str:
    if i not in hex:
        la_hex = False

if la_hex:
    print(int(str ,16))
else:
    hex_sau_khi_loc = "" 
    for j in hex:
        hex_sau_khi_loc =  hex_sau_khi_loc +j
print(hex_sau_khi_loc)
print(int(hex_sau_khi_loc , 16))

