ChieuCao = (161, 182, 161, 154, 176, 170, 167, 171, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
            162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170)
# a. Có bao nhiêu sinh viên:
print("Số lượng sinh viên:", len(ChieuCao))
# b. Chiều cao trung bình:
TB = sum(ChieuCao) / len(ChieuCao)
print("Chiều cao trung bình:", TB)
# c. Liệt ra các chiều cao khác nhau trong nhóm và in ra chiều cao trung bình của nhóm:
ChieuCaoKhacNhau = set(ChieuCao)
print("Các chiều cao khác nhau:", ChieuCaoKhacNhau)
print("Chiều cao trung bình của nhóm:", sum(ChieuCaoKhacNhau) / len(ChieuCaoKhacNhau))