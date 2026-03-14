d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
    if d < 31:
        d = d + 1
    else:
        d = 1
        m = m + 1
elif m == 4 or m == 6 or m == 9 or m == 11:
    if d < 30:
        d = d + 1
    else:
        d = 1
        m = m + 1
elif m == 2:
    if d < 28:
        d = d + 1
    else:
        d = 1
        m = m + 1
elif m == 12:
    if d < 31:
        d = d + 1
    else:
        d = 1
        m = 1
        y = y + 1
print("Ngày tiếp theo là:", d, "/", m, "/", y)