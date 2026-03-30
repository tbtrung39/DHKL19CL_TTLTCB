#tìm giá trị ASCII của một ký tự
ky_tu = input("Nhập một ký tự: ")
if len(ky_tu) != 1:
    print("Vui lòng nhập một ký tự duy nhất.")
else:
    ascii_value = ord(ky_tu)
    print(f"Giá trị ASCII của ký tự '{ky_tu}' là: {ascii_value}")