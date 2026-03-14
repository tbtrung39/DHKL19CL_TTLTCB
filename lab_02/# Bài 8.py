# Bài 8:
n = input("Nhập thâm niên (tháng): ")
nl = int(n)
luong_cb = 1350000
if nl < 12:
    print("Lương của bạn là: ", luong_cb)
elif nl >= 12 and nl < 36:
    print("Lương của bạn là: ", luong_cb * 1.1)
elif nl >= 36 and nl < 60:
    print("Lương của bạn là: ", luong_cb * 1.2)
elif nl >= 60 and nl < 120:
    print("Lương của bạn là: ", luong_cb * 1.3)
else:
    print("Lương của bạn là: ", luong_cb * 1.5)
    
    