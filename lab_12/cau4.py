try:
    file_doc = input("Nhap ten file can doc: ")
    with open(file_doc, "r", encoding="utf-8") as file1:
        noi_dung = file1.read()
    file_ghi = input("Nhap ten file can ghi: ")
    with open(file_ghi, "w", encoding="utf-8") as file2:
        file2.write(noi_dung)
    print("Da sao chep noi dung sang file moi")
except FileNotFoundError:
    print("Loi: File khong ton tai!")
except ValueError:
    print("Loi mo sai che do file!")
except Exception:
    print("Co loi xay ra:")