try:
    ten_file = input("Nhap ten tap tin: ")
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    print("Noi dung tap tin:")
    print(noi_dung)

    with open(r"bai3\copy.dat", "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print("Da ghi vao tap tin copy.dat thanh cong!")
except FileNotFoundError:
    print("Khong tim thay tap tin '{}'!".format(ten_file))
    print("Ket thuc chuong trinh.")