ky_tu = input("Nhập một ký tự bất kỳ: ")
if len(ky_tu) == 1:
    print(f"Giá trị ASCII của '{ky_tu}' là: {ord(ky_tu)}")
else:
    print("Vui lòng chỉ nhập duy nhất một ký tự.")