ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang == 2:
    max = 28
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    max = 30
else:
    max = 31

if ngay < max:
    ngay += 1
else:
    ngay = 1
    if thang == 12:
        thang = 1
    else:
        thang += 1

print("Ngày tiếp theo:", ngay, "/", thang)