# Khai báo các chuỗi
chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Bóng rổ"]

print("Các câu được tạo ra là:")
for cn in chu_ngu:
    for dt in dong_tu:
        for tn in tan_ngu:
            cau_hoan_chinh = cn + " " + dt + " " + tn
            print(cau_hoan_chinh)