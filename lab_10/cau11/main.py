from doicoso import doicoso1
from doicoso import doicoso2
n = doicoso1.nhap_so()
print("He nhi phan:", doicoso1.nhi_phan(n))
print("He bat phan:", doicoso1.bat_phan(n))
print("He thap luc phan:", doicoso1.thap_luc_phan(n))
s = input("Nhap chuoi: ")
chuoi = doicoso2.loc_ky_tu(s)
print("Chuoi sau khi loc:", chuoi)
co_so = doicoso2.kiem_tra(chuoi)
print("Co so:", co_so)
if co_so != "Khong xac dinh":
    he10 = doicoso2.sang_he_10(chuoi, co_so)
    print("Gia tri he 10:", he10)