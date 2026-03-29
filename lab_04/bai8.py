ky_tu = input("Nhập 1 kí tự: ")
while len(ky_tu) != 1:
    ky_tu = input("Nhập lại (chỉ 1 ký tự): ")
print("Mã ACSII là: ", ord(ky_tu))
