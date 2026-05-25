import doicoso2
s = input("Nhap chuoi: ")
chuoi = doicoso2.loc_ky_tu(s)
print("Chuoi sau khi loc:", chuoi)
co_so = doicoso2.kiem_tra(chuoi)
print("Co so cua chuoi la:", co_so)
if co_so != "Khong xac dinh":
    he10 = doicoso2.sang_he_10(chuoi, co_so)
    print("Gia tri he 10:", he10)