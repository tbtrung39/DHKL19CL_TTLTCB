diem = float(input("Nhập điểm TK (0-10): "))
if 0 <= diem < 3:
    print("Loại Kém")
elif diem < 4:
    print("Loại Yếu")
elif diem < 5:
    print("Loại Yếu")  # 4.0 -> 5.0 gap (theo đề bài để nguyên)
elif diem < 7:
    print("Loại Trung bình")
elif diem < 8:
    print("Loại Khá")
elif diem < 9:
    print("Loại Giỏi")
elif diem <= 10:
    print("Loại Xuất sắc")
else:
    print("Điểm không hợp lệ")