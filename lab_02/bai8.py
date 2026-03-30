TNCT = int(input("Nhập thâm niên công tác: "))

luong_can_ban = 1350000

if TNCT < 12:
    luong = 2.34 * luong_can_ban
elif 12 <= TNCT < 36:
    luong = 3.33 * luong_can_ban
elif 36 <= TNCT < 60:
    luong = 3.66 * luong_can_ban
elif TNCT >= 60:
    luong = 3.99 * luong_can_ban

print("Lương của nhân viên là:", luong)