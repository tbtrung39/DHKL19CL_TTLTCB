Str1 = input("Nhập chuỗi 1: ")
Str2 = input("Nhập chuỗi 2: ")
ket_qua = ""
if len(Str1) > len(Str2):
    max_len = len(Str1)
else:
    max_len = len(Str2)
    for i in range(max_len):
        if i < len(Str1):
            ket_qua = ket_qua + Str1[i]
        if i < len(Str2):
            ket_qua = ket_qua + Str2[i]
    print("Chuỗi kết quả:", ket_qua)