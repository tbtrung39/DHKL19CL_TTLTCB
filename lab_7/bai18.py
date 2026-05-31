thi_sinh_db = {
    "SBD001": {"ho_ten": "Nguyen Van A", "diem_thi": 8.5},
    "SBD002": {"ho_ten": "Le Thi B", "diem_thi": 7.0}
}

sbd_tra_cuu = input("Nhập số báo danh cần tra cứu: ")

if sbd_tra_cuu in thi_sinh_db:
    # Nếu tồn tại thí sinh
    print("--- Kết quả tra cứu ---")
    print(f"Họ và tên: {thi_sinh_db[sbd_tra_cuu]['ho_ten']}")
    print(f"Điểm thi: {thi_sinh_db[sbd_tra_cuu]['diem_thi']}")
else:
    print("Không tìm thấy số báo danh này! Vui lòng bổ sung thông tin:")
    ho_ten_moi = input("Nhập họ và tên thí sinh mới: ")
    diem_moi = float(input("Nhập điểm thi: "))
thi_sinh_db[sbd_tra_cuu] = {"ho_ten": ho_ten_moi, "diem_thi": diem_moi}
print(f"Đã bổ sung thành công thí sinh {sbd_tra_cuu} vào hệ thống!")    