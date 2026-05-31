def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_ket_qua(ho_ten, dtb):
    print(f"Sinh viên: {ho_ten} -> Điểm trung bình: {dtb:.2f}")

# Sử dụng các hàm phối hợp
ten, t, l, h = nhap_thong_tin()
diem_tb = tinh_trung_binh(t, l, h)
xuat_ket_qua(ten, diem_tb)