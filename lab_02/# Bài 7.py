# Bài 7:
diem = input("Nhập điểm TK: ")
diem_so = float(diem)
if diem_so < 3:
    print("Học lực kém")
elif diem_so < 5:
    print("Học lực yếu")
elif diem_so < 7:
    print("Học lực trung bình")
elif diem_so < 8:
    print("Học lực khá")
elif diem_so < 9:
    print("Học lực giỏi")
else:
    print("Học lực xuất sắc")