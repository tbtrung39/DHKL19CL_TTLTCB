s = input("Nhập chuỗi Hex: ").upper()
hex_chars = "0123456789ABCDEF"
hex_only = "".join([c for c in s if c in hex_chars])

if not hex_only:
    print("Không có ký tự Hex hợp lệ.")
else:
    thap_phan = int(hex_only, 16)
    print(f"Chuỗi Hex hợp lệ: {hex_only}")
    print(f"Giá trị thập phân: {thap_phan}")