tnct = input("Nhập thâm niên (tháng): ")
tnct_l = int(tnct)
luong_cb = 1350000
if tnct_l < 12:
    he_so = 2.34
elif 12 <= tnct_l < 36:
    he_so = 3.33
elif 36 <= tnct_l < 60:
    he_so = 3.66
elif tnct_l >= 60:
    he_so = 3.99
luong = he_so * luong_cb
print(f"Lương của nhân viên là: {luong} VNĐ")
