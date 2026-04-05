s = input("Nhập chuỗi: ").upper
hex_chars = "0123456789ABCDEF"
hop_le = True
for c in s:
    if c not in hex_chars:
        hop_le = False
if hop_le:
    print("Là chuỗi Hex")
    print("Giá trị thập phân: ", int(s, 16))
else:
    s_moi = ""
    for c in s:
        if c in hex_chars:
            s_moi += c
    print("Chuỗi sau khi lọc: ", s_moi)
    if s_moi != "":
        print("Thập phân: ", int(s_moi, 16))