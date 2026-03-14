'''
Viết 1 chương trình tính lương của nhân viên dựa theo thâm niên công tác(TNCT)
Lương = hệ số * lương căn bản, lương căn bản là 1tr350k
 + Nếu TNCT < 12th: hệ số = 2.34
 + Nếu 12th <= TNCT <= 36th: hệ số = 3.33
 + Nếu 36th <= TNCT <= 60th: hệ số = 3.66
 + Nếu TNCT >= 60th: hệ số = 3.99
'''
tnct = float(input("Nhập thâm niên công tác: "))
l = 1350000
if tnct < 12:
    luong = 2.34 * l
    print("Lương nhận được: ",luong)
elif 12 <= tnct <= 36:
    luong = 3.33 * l
    print("Lương nhận được: ", luong)
elif 36 <= tnct <= 60:
    luong = 3.66 * l
    print("Lương nhận được: ", luong)
else:
    luong = 3.99 * l
    print("Lương nhận được là: ", luong)