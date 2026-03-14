# Bài 5:
thang = input("Nhập tháng (1-12): ")
n_thang = int(thang)
if n_thang == 1:
    print("Tháng 1 có 31 ngày.")
elif n_thang == 2:
    print("Tháng 2 có 28 hoặc 29 ngày.")
elif n_thang == 3:
    print("Tháng 3 có 31 ngày.")
elif n_thang == 4:
    print("Tháng 4 có 30 ngày.")
elif n_thang == 5:
    print("Tháng 5 có 31 ngày.")
elif n_thang == 6:
    print("Tháng 6 có 30 ngày.")
elif n_thang == 7:
    print("Tháng 7 có 31 ngày.")
elif n_thang == 8:
    print("Tháng 8 có 31 ngày.")
elif n_thang == 9:
    print("Tháng 9 có 30 ngày.")
elif n_thang == 10:
    print("Tháng 10 có 31 ngày.")
elif n_thang == 11:
    print("Tháng 11 có 30 ngày.")
elif n_thang == 12:
    print("Tháng 12 có 31 ngày.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập số từ 1 đến 12.")