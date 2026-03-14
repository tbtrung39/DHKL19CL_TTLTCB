tnct = int(input("Nhập thâm niên ( số tháng đã làm ): ")) 
luong_cb = 1350000

if tnct < 12:
    hs = 2.34
elif tnct < 36:
    hs = 3.33
elif tnct < 60:
    hs = 3.66
else:
    hs = 3.99

luong = hs * luong_cb

print("Lương:", luong, "đồng")