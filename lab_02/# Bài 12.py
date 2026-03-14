# Bài 12:
ngay = input("Nhập ngày: ")
ngay_t = int(ngay)
thang = input("Nhập tháng (1-12): ")
thang_t = int(thang)
if thang_t == 2:
    max_ngay = 28
elif thang_t == 4 or thang_t == 6 or thang_t == 9 or thang_t == 11:
    max_ngay = 30
else:
    max_ngay = 31
if ngay_t < max_ngay:
    ngay_t = ngay_t + 1
else:
    ngay_t = 1
    thang_t = thang_t + 1
    if thang_t > 12:
        thang_t = 1
print(f"Ngày tiếp theo là: {ngay_t}/{thang_t}") 