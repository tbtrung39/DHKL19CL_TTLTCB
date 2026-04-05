Str = input("Nhập chuỗi nhị phân: ")
ket_qua = 0
for i in range(len(Str)):
    ky_tu = Str[len(Str) - 1 - i]
    gia_tri = int(ky_tu)
    ket_qua = ket_qua + gia_tri * (2 ** i)
print("Dạng thập phân:", ket_qua)