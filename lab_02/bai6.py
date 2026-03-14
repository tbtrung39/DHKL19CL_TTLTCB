x = int(input("Nhập số nguyên có 3 chữ số: "))

so = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]

if x < 100 or x > 999:
    print("Vui lòng nhập số nguyên có 3 chữ số!")
else:
    hang_tram = x // 100
    hang_chuc = (x % 100) // 10
    hang_don_vi = x % 10

    doc_so = so[hang_tram] + " trăm"

    if hang_chuc == 0 and hang_don_vi == 0:
        pass
    elif hang_chuc == 0:
        doc_so += " linh " + so[hang_don_vi]
    elif hang_chuc == 1:
        doc_so += " mười"
        if hang_don_vi != 0:
            doc_so += " " + so[hang_don_vi]
    else:
        doc_so += " " + so[hang_chuc] + " mươi"
        if hang_don_vi != 0:
            doc_so += " " + so[hang_don_vi]
    print(doc_so)
