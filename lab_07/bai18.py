data_thi = {"001": {"ten": "An", "diem": 8}, "002": {"ten": "Ba", "diem": 7}}
sbd = input("\nNhập SBD cần tra (Bài 18): ")

found = False
for k in data_thi:
    if k == sbd:
        print(f"Họ tên: {data_thi[k]['ten']}, Điểm: {data_thi[k]['diem']}")
        found = True
        break

if not found:
    print("Không tìm thấy, vui lòng nhập mới:")
    ten_moi = input("Họ tên: ")
    diem_moi = float(input("Điểm: "))
    data_thi[sbd] = {"ten": ten_moi, "diem": diem_moi}