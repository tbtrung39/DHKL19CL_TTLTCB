van_ban = input("Nhập đoạn văn bản: ")
tu_can_tim = input("Nhập từ cần tìm: ")

# Tách văn bản thành danh sách các từ
danh_sach_tu = van_ban.split()
dem = danh_sach_tu.count(tu_can_tim)

print(f"Từ '{tu_can_tim}' xuất hiện {dem} lần.")