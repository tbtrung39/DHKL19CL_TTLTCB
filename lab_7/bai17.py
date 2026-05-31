sinh_vien_dict = {}

n = int(input("Nhập số lượng sinh viên: "))
for i in range(n):
    print(f"\n--- Nhập sinh viên thứ {i+1} ---")
    while True:
        ma_sv = input("Mã sinh viên (6 ký tự số): ")
        if len(ma_sv) == 6 and ma_sv.isdigit():
            break
        print("Mã số không hợp lệ! Vui lòng nhập đúng 6 ký tự số.")
        
    ten_sv = input("Họ và tên sinh viên: ")
    diem = round(float(input("Nhập điểm số: "))) # Làm tròn thành số nguyên
    
    # Lưu vào dictionary với Key là mã số, Value là một dict con chứa tên và điểm
    sinh_vien_dict[ma_sv] = {"ten": ten_sv, "diem": diem}

# Sắp xếp từ điển theo giá trị điểm giảm dần
# Hàm sorted trả về một danh sách các Key đã sắp xếp dựa trên điểm số
ma_sv_sap_xep = sorted(sinh_vien_dict, key=lambda x: sinh_vien_dict[x]["diem"], reverse=True)

print("\n=== THỐNG KÊ SINH VIÊN THEO ĐIỂM GIẢM DẦN ===")
for ma in ma_sv_sap_xep:
    print(f"Mã SV: {ma} | Tên: {sinh_vien_dict[ma]['ten']} | Điểm: {sinh_vien_dict[ma]['diem']}")