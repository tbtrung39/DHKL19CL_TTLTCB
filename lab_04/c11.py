chuoi = input("Nhập chuỗi nhị phân: ")

ket_qua = 0
vi_tri = 0
hop_le = True

while vi_tri < len(chuoi):
    ky_tu = chuoi[vi_tri]
    if ky_tu == '0' or ky_tu == '1':
        ket_qua = ket_qua * 2 + int(ky_tu)
    else:
        hop_le = False
        break

    vi_tri = vi_tri + 1

if hop_le:
    print("Số thập phân là:", ket_qua)
else:
    print("Chuỗi không hợp lệ")